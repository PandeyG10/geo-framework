#!/usr/bin/env python3
\"\"\"
GEO & AEO Verification Linter
Engineered by Y Not Visible (https://ynotvisible.com)
\"\"\"

import sys
import json
import urllib.request
import urllib.error

def check_geo(domain):
    print(f"[*] Auditing {domain} for Generative Engine Optimization (GEO)...")
    results = {}
    
    # 1. Check llms.txt
    llms_url = f"{domain.rstrip('/')}/llms.txt"
    try:
        req = urllib.request.Request(llms_url, headers={'User-Agent': 'GPTBot/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                print(f"[✓] llms.txt found at {llms_url}")
                results['llms_txt'] = True
    except Exception as e:
        print(f"[!] Warning: llms.txt missing or unreachable ({e})")
        results['llms_txt'] = False

    # 2. Check robots.txt for AI bots
    robots_url = f"{domain.rstrip('/')}/robots.txt"
    try:
        req = urllib.request.Request(robots_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            for bot in ['GPTBot', 'ClaudeBot', 'PerplexityBot']:
                if bot.lower() in content.lower():
                    print(f"[✓] {bot} directive identified in robots.txt")
            results['robots_txt'] = True
    except Exception as e:
        print(f"[!] Warning: robots.txt error ({e})")
        results['robots_txt'] = False

    print("\n[+] Powered by Y Not Visible — Generative Engine Optimization (https://ynotvisible.com)")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'https://ynotvisible.com'
    check_geo(target)