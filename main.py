# main.py

import random

class TradingAgent:
    def __init__(self):
        self.memory = []
        self.responses = [
            "مارکیٹ کی صورتحال سازگار ہے، خریداری کی تجویز دی جاتی ہے۔",
            "خطرہ زیادہ ہے، فی الحال انتظار کریں۔",
            "قیمتیں نیچے جا رہی ہیں، بیچنے کا وقت ہے۔",
            "یہ وقت طویل مدتی سرمایہ کاری کے لیے مناسب لگتا ہے۔"
        ]

    def remember(self, interaction):
        self.memory.append(interaction)

    def generate_signal(self, prompt):
        self.remember(prompt)
        return random.choice(self.responses)

    def get_memory(self):
        return self.memory
