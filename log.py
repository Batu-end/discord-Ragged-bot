import sqlite3
from datetime import datetime

# connect to database
connect = sqlite3.connect("data/message_logs.db")

# cursor lets us use commands on the database
cursor = connect.cursor()

# table with 4 columns: user_id, channel_id, timestamp and message_length
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    user_id TEXT,
    channel_id TEXT,
    timestamp TEXT,
    message_length INTEGER
)
""")
connect.commit()

# function to log each message
def log_messages(message):
    cursor.execute("""
    INSERT INTO messages (user_id, channel_id, timestamp, message_length)
    VALUES (?, ?, ?, ?)
""", (
        str(message.author.id),
        str(message.channel.id),
        datetime.utcnow().isoformat(),
        len(message.content)
    ))
    connect.commit()