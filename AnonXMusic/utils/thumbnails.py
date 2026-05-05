import random

# 🔥 Tumhare diye hue images
RANDOM_THUMBS = [
    "https://files.catbox.moe/ikxb96.jpg",
    "https://files.catbox.moe/dqxsjh.jpg",
    "https://files.catbox.moe/lnaqxk.jpg",
    "https://files.catbox.moe/auxh1p.jpg",
    "https://files.catbox.moe/lz57vi.jpg",
    "https://files.catbox.moe/x1fcb6.jpg",
    "https://files.catbox.moe/32ghsc.jpg",
    "https://files.catbox.moe/tm8vmd.jpg",
    "https://files.catbox.moe/n19sa7.jpg",
    "https://files.catbox.moe/jf2cr9.jpg",
    "https://files.catbox.moe/exmypk.jpg",
    "https://files.catbox.moe/mcd1pu.jpg",
    "https://files.catbox.moe/4scao5.jpg",
    "https://files.catbox.moe/58zkf9.jpg",
    "https://files.catbox.moe/svzu50.jpg",
    "https://files.catbox.moe/wzgrks.jpg",
]

_last_thumb = None


async def get_thumb(videoid=None, user_id=None):
    global _last_thumb

    try:
        choice = random.choice(RANDOM_THUMBS)

        if len(RANDOM_THUMBS) > 1:
            while choice == _last_thumb:
                choice = random.choice(RANDOM_THUMBS)

        _last_thumb = choice
        return choice

    except Exception as e:
        print(f"Thumb Error: {e}")
        return RANDOM_THUMBS[0]
