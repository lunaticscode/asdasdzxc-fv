
const API_PATH = {
    ARTICLE_LIST: "/article/all",
    ARTICLE_UPLOAD: "/article/upload"
}

const getProdList = async() => {
    try{
        return await fetch(API_PATH.ARTICLE_LIST, {
            method: "get",
            headers: {"Content-Type" : "application/json"}
        }).then(res => res.json())
        .then(res => res)
        .catch(err => {console.log({err}); return [];})
    }
    catch(err){
        console.log({err});
        return []
    }
}

const isValidListData = (data) => {
    return !data || Array.isArray(data) || !data.length
}

const handleClickProdItem = (_id) => {
    location.href = `./article?id=` + _id
}

const prodListRootElem = document.getElementById("prod_list_root");

const renderingProdList = (prodList) => {
    let addedProdItems = '';
    prodList.forEach((prod, index) => {
        const prodItemHtml = `
            <div class='prod_item_wrapper' onclick='handleClickProdItem("${prod._id}")' >
                <div class='prod_title'>${prod.title}</div>
                <div class='prod_desc'>${prod.description}</div>
            </div>
        `
        addedProdItems = addedProdItems + prodItemHtml;
    })
    prodListRootElem.innerHTML = addedProdItems;
}

window.document.addEventListener("DOMContentLoaded", async () => {
     const { data, isError } = await getProdList();
     if(isError) return;
     if(!data || !Array.isArray(data) || !data.length) return;
     console.log({data})
     renderingProdList(data)

})