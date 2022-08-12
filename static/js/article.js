
const getArticleDetailData = async (id) => {
   try{
    return await fetch("/article/detail?id="+id, {
        headers: {"Content-Type": "application/json"}
    }).then(res => res.json())
    .then(res => res)
    .catch(err => {console.log({err}); return null})
   }
   catch(err){
        console.log({err});
        return null;
   }
}

const articleDetailWrapperElem =  document.getElementById("prod_detail_wrapper");
const renderingArticleDetail = (data) => {
    const contentHtml = `
        <div id='article_title'>${data.title}</div>
        <div id='article_desc'>${data.description}</div>
        <div id='article_img_wrapper'>
            <img id='article_img' src="data:image/jpeg; base64, ${data.imgSrc}" />
        </div>
    `
    articleDetailWrapperElem.innerHTML = contentHtml;
}

const getArticleId = async() => {
    const params = new URLSearchParams(window.location.search)
    const id = params.get("id") || null;
    if(!id) {
        alert("잘못된 데이터 형식입니다.");
        location.href = "/";
    }
    const {data, isError} = await getArticleDetailData(id);
    if(!data || isError) {
        alert("해당 글의 id는 존재하지 않습니다.")
        location.href = "/";
    }
    renderingArticleDetail(data)
}

document.addEventListener("DOMContentLoaded", () => {
    getArticleId()
})