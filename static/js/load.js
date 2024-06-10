document.addEventListener("DOMContentLoaded", () => {
    let spans = document.getElementsByClassName("footer_year");

    // 获取当前年份
    let d = new Date();
    let y = d.getFullYear();

    // 遍历所有匹配的元素并更新内容
    Array.from(spans).forEach(span => {
        span.textContent = `${y}`;
    }, 2000);

    // document.getElementById("load").style.display = "none";
});




window.addEventListener("load", () => {
    // 隐藏载入动画
    setTimeout(() => {
        document.getElementById("load").style.display = "none";
    }, 1000); 
});

// 每次頁面重新載入時顯示載入動畫
window.addEventListener('beforeunload', () => {
    document.getElementById("load").style.display = "block";
});