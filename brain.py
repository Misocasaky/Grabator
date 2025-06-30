def respond_to_user(text):
    text = text.lower()

    if "شطرنج" in text:
        return "♟️ الشطرنج هي لعبة استراتيجية تتطلب تفكيراً عميقاً وتخطيطاً مسبقاً."
    elif "حب" in text:
        return "💖 الحب شعور لا يُوصف، لكنه يُحس... وقد يغير حياتك!"
    elif "ذكاء" in text or "grabator" in text:
        return "🧠 أنا Grabator، أتعلم من محادثاتك وأتحسن يوماً بعد يوم."
    else:
        return "🤔 لم أفهم قصدك تماماً، لكني أتعلم مع كل رسالة."
