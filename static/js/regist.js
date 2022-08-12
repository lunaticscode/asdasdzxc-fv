const imgSelectorElem = document.getElementById("img_selector")

imgSelectorElem.addEventListener('change', function(event) {
    const src = event.target.files[0];
    const fileReader = new FileReader();
    fileReader.onload = function(){
        const previewElem = document.getElementById("img_preview");
        previewElem.src = fileReader.result
    }
    fileReader.readAsDataURL(src)
})