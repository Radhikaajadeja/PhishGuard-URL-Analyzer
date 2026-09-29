from urllib.parse import urlparse
import re


def analyze_url(url):
    risks = []
    score = 0

    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    # 1. HTTPS check
    if parsed.scheme != "https":
        risks.append("No HTTPS connection")
        score += 25

    # 2. IP address check
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
        risks.append("IP address used instead of domain name")
        score += 25

    # 3. @ symbol check
    if "@" in url:
        risks.append("URL contains @ symbol")
        score += 20

    # 4. URL length check
    if len(url) > 100:
        risks.append("Unusually long URL")
        score += 10

    # 5. Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "account",
        "password",
        "update",
        "secure",
        "bank"
    ]

    found_words = [
        word for word in suspicious_words
        if word in url.lower()
    ]

    if found_words:
        for word in found_words:
            risks.append(f"Suspicious keyword detected: {word}")

        score += min(len(found_words) * 5, 20)

    # Maximum score = 100
    score = min(score, 100)

    # Risk level
    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, risks


# ==============================
# PHISHGUARD APPLICATION
# ==============================

print("=" * 55)
print("        🔐 PHISHGUARD - URL SECURITY ANALYZER")
print("=" * 55)

url = input("\nEnter a URL to analyze: ")

score, level, risks = analyze_url(url)

print("\n🔍 Analysis Result")
print("-" * 35)

print(f"Risk Score: {score}/100")
print(f"Risk Level: {level}")

print("\nDetected Indicators:")

if risks:
    for risk in risks:
        print("⚠️", risk)
else:
    print("✅ No obvious phishing indicators detected.")

print("\nRecommendation:")

if level == "HIGH":
    print("🚨 Treat this URL with caution.")
elif level == "MEDIUM":
    print("⚠️ Verify the website before entering sensitive information.")
else:
    print("✅ No obvious phishing indicators detected.")

print("\nNote: This is an educational tool.")
print("It cannot guarantee that a URL is safe or malicious.")