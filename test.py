def mapping_item_img(item):
    item["img_id"] = 'img-id'
    return item
_list = [{"title": "asd"}]
after_list = map(mapping_item_img, _list)
print(list(after_list))