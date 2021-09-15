frappe.listview_settings['Asset'] = {
    onload(listview) {
        this.add_button("Download Barcode", "default", function () {
            const docnames = cur_list.get_checked_items(true);
            if(docnames.length <= 0)
                frappe.throw("Please Select one or more Asset Docs")
            
            frappe.call({
                method:"nub.api.download_multi_pdf",
                args:{
                    docnames: docnames,
                },
                callback: function(r){
                    if(r.message && r.message.name){
                        window.open(`#Form/Asset%20Printer/${r.message.name}`, '_blank')
                    }
                }
            })
        })
    },
    add_button(name, type, action, wrapper_class = ".page-actions") {
        const button = document.createElement("button");
        button.classList.add("btn", "btn-" + type, "btn-sm", "ml-2");
        button.innerHTML = name;
        button.onclick = action;
        document.querySelector(wrapper_class).prepend(button);
    }
}