---
title: 
---
這個部落格始於 2025/12/30。早於這個時間的貼文都是從別處的筆記遷移過來的。

我會在這個部落格寫一些軟體使用相關的筆記，也會把一些大學學科的筆記同步進來。

---

部落格在 2026/2/2 遷移到 Fuwari/Astro。

::github{repo="minstrike520/blog-fuwari"}

---

> ### Sources of images used in this site
> - [Unsplash](https://unsplash.com/)
> - [星と少女](https://www.pixiv.net/artworks/108916539) by [Stella](https://www.pixiv.net/users/93273965)
> - [Rabbit - v1.4 Showcase](https://civitai.com/posts/586908) by [Rabbit_YourMajesty](https://civitai.com/user/Rabbit_YourMajesty)

---

### 友鏈

<style>
/* 1. 父容器：確保子元素可以被拉伸 */
.banner-container {
    display: flex;
    gap: 0em;
    /* 改用 stretch，這會讓所有 <a> 標籤自動變成一樣高（以最高的那個為準） */
    align-items: stretch; 
    justify-content: center;
}

/* 2. 連結標籤：變成 Flex 容器來置中圖片 */
.banner-container a {
    display: flex !important;       /* 必須是 flex 才能響應父層的 stretch */
    align-items: center;           /* 讓圖片在 <a> 裡面垂直置中 */
    justify-content: center;       /* 讓圖片在 <a> 裡面水平置中 */
    padding: 0 !important;
    margin: 0 !important;
    border: 1px solid transparent; /* 技巧：加個透明邊框有助於排版穩定，或依需求換成實色 */
    text-decoration: none;
    height: 2em;
}

/* 3. 圖片：消除所有干擾高度的因素 */
.banner-container img {
    display: block !important;
    margin: 0 !important;          /* 徹底消除之前的 32px 影響 */
    max-height: 100%;              /* 確保圖片不會超出 <a> 的範圍 */
    height: auto;
    pointer-events: none;
    border-radius: 0 !important;
}
</style>

<center>
<div class="banner-container">
    <a title='ヤチヨの部屋' href="https://yachiyo.net/#/">
        <img src="/yachiyo_net_banner_jp.gif" alt="ヤチヨの部屋バナー" class="banner-img">
    </a>
    <a title='Diggon lol' href="https://diggon.lol/">
        <img src="https://diggon.lol/pictures/icons/88x31.gif">
    </a>
</div>
</center>
