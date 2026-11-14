#!/usr/bin/env python3
"""颜文字生成器 - 随机组装各种心情的颜文字 ◕‿◕"""

import random
import sys

MOODS = {
    "开心": {
        "eyes": ["◕", "◠", "＾", "˶ᵔ", "≧", "☆", "•̀", "¬", "◡"],
        "mouths": ["‿", "▽", "ω", "∀", "ᵕ", "︶", "▿"],
        "arms": [("", ""), ("ヽ", "ノ"), ("٩", "۶"), ("o", "o"), ("☆", "☆"), ("＼", "／")],
    },
    "难过": {
        "eyes": ["´•", "╥", "T", "；", "个", "ಥ", "泣", "╯"],
        "mouths": ["﹏", "︵", "ヘ", "△", "Д", "_"],
        "arms": [("", ""), ("(", ")"), ("。゜", "゜。"), ("", "…")],
    },
    "生气": {
        "eyes": ["╬", "`д", "＃`", "ಠ", "凸", "눈", "`Д"],
        "mouths": ["皿", "Д", "益", "へ", "ヘ", "д"],
        "arms": [("", ""), ("(╯", ")╯", ), ("凸", "凸"), ("ヽ", "ノ")],
    },
    "疑惑": {
        "eyes": ["・", "？", "◉", "⊙", "¿", "0", "o"],
        "mouths": ["_", "ヘ", "。", "ω", "▂", "~"],
        "arms": [("", "?"), ("(", ")?"), ("", "???"), ("┐", "┌")],
    },
    "害羞": {
        "eyes": ["⁄⁄•", "˶′", "♡", "〃", "p", "⺣"],
        "mouths": ["⁄⁄", "ω", "ᵕ", "﹃", "▽", "³"],
        "arms": [("", ""), ("(", ")"), ("", "♡"), ("♡", "♡")],
    },
}

FACES = ["({l}{m}{r})", "( {l}{m}{r} )", "({l} {m} {r})", "[{l}{m}{r}]"]


def generate(mood_name, count=5):
    mood = MOODS[mood_name]
    results = set()
    tries = 0
    while len(results) < count and tries < count * 50:
        tries += 1
        left = random.choice(mood["eyes"])
        right = random.choice(mood["eyes"])
        mouth = random.choice(mood["mouths"])
        arm_l, arm_r = random.choice(mood["arms"])
        face = random.choice(FACES).format(l=left, m=mouth, r=right)
        results.add(f"{arm_l}{face}{arm_r}")
    return list(results)


def main():
    mood_names = list(MOODS.keys())

    if len(sys.argv) > 1:
        chosen = sys.argv[1]
        if chosen not in MOODS:
            print(f"未知心情: {chosen}")
            print(f"可用心情: {', '.join(mood_names)}")
            sys.exit(1)
        moods_to_show = [chosen]
    else:
        moods_to_show = mood_names

    count = 5
    if len(sys.argv) > 2:
        count = int(sys.argv[2])

    for mood_name in moods_to_show:
        print(f"\n{'=' * 30}")
        print(f"  【{mood_name}】颜文字")
        print(f"{'=' * 30}")
        for i, face in enumerate(generate(mood_name, count), 1):
            print(f"  {i}. {face}")

    print(f"\n用法: python emoticon_generator.py [心情] [数量]")
    print(f"可用心情: {', '.join(mood_names)}")


if __name__ == "__main__":
    main()
