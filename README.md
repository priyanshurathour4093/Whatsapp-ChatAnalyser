
# 📊 WhatsApp Chat Analyzer

A Streamlit-based tool to uncover insights from your exported WhatsApp chats. Upload a `.txt` file, pick a user, and get instant visual analysis — messages, words, emojis, timelines, and more.

---

## 🔍 Features

- **Total Stats**: Messages, words, media, links  
- **Monthly & Daily Timeline**: Track chat activity over time  
- **Activity Maps**:  
  - Busiest days and months  
  - Hourly heatmap  
- **Most Active Users**: Top contributors in group chats  
- **WordCloud**: Most frequent words (after removing Hinglish stopwords)  
- **Most Common Words**: Top 20 words used  
- **Emoji Analysis**: Most-used emojis with pie chart  
- **URL Tracking**: Total links shared  

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the App

```bash
streamlit run app.py
```

The app will open in your browser. Upload the exported WhatsApp `.txt` file and explore.

---

## 📁 Project Structure

```
📦 whatsapp-chat-analyzer/
├── app.py              # Main Streamlit frontend
├── helper.py           # All feature logic (stats, charts, etc.)
├── preprocessor.py     # Message parsing and timestamp formatting
├── stop_hinglish.txt   # Stop words used in word cloud filtering
├── requirements.txt    # Python packages needed
```

---

## 📝 How to Export WhatsApp Chat

1. Open a chat on WhatsApp (mobile)  
2. Tap ⋮ > More > Export Chat  
3. Choose **Without Media**  
4. It generates a `.txt` file — upload it in the app  

---

## 📦 Dependencies

This project uses:

- streamlit  
- matplotlib  
- seaborn  
- pandas  
- emoji  
- wordcloud  
- urlextract  

Install them with:
```bash
pip install -r requirements.txt
```

---

