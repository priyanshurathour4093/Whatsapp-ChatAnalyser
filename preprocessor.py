import re
import pandas as pd

def preprocess(data):
    # Regex pattern for timestamps like [13/02/25, 00:50:49] 
    pattern = r'\[\d{2}/\d{2}/\d{2},\s\d{2}:\d{2}:\d{2}\]\s'

    messages = re.split(pattern, data)[1:]  # first split is empty string
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Parse datetime with matching format including brackets and seconds
    df['message_date'] = pd.to_datetime(df['message_date'], format='[%d/%m/%y, %H:%M:%S] ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # username present
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:  # group notification/system message
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Additional datetime attributes for analysis
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour+1}")
    df['period'] = period

    return df
