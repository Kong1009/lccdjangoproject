document.addEventListener("DOMContentLoaded", () => {
    let spans = document.getElementsByClassName("footer_year");

    // 获取当前年份
    let d = new Date();
    let y = d.getFullYear();

    // 遍历所有匹配的元素并更新内容
    Array.from(spans).forEach(span => {
        span.textContent = `${y}`;
    });
});
