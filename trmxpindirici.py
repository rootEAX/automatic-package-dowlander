import subprocess
import sys

def install(pkg):
    print(f"[+] Yükleniyor: {pkg}")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

print("\n[+] pip güncelleniyor...\n")
subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

packages = [
    # Temel
    "requests",
    "beautifulsoup4",
    "lxml",
    "aiohttp",
    "colorama",
    "tqdm",

    # Ağ & Analiz
    "scapy",
    "python-nmap",
    "dnspython",
    "netaddr",

    # Web Güvenliği
    "selenium",
    "webdriver-manager",
    "urllib3",
    "fake-useragent",

    # Kripto / Parola / CTF
    "pwntools",
    "passlib",
    "pycryptodome",

    # OSINT
    "shodan",
    "whois",
    "googlesearch-python",

    # AI & Otomasyon
    "openai",
    "python-dotenv"
]

print("[+] Etik hacking paketleri yükleniyor...\n")

for pkg in packages:
    install(pkg)

print("\n[✓] TÜM ETİK HACKERLIK PYTHON PAKETLERİ HAZIR!")
