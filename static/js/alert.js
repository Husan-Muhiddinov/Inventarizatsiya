function confirm_category_delete(pk, name){
    Notiflix.Confirm.show(
        "Warning!", 
        name + ' ' + "nomli modelni o'chirmoqchimisiz?", 
        "Yes", 
        "No",
        function okCb() {
            Notiflix.Report.success(
                'Success',
                'Item deleted successfully!',
                'Okay',
                () => {
                    window.location.href="/-V--3.0.5/category-delete/"+ pk +""
                },);
        },
        function cancelCb() {
            Notiflix.Report.failure('Failure', name + ' was saved!', 'Okay');
        },
        );
}

function confirm_model_delete(pk, name){
    var r = Notiflix.Confirm.show(
        "Warning!", 
        name + ' ' + "nomli modelni o'chirmoqchimisiz?", 
        "Yes", 
        "No",
        function okCb() {
            Notiflix.Report.success(
                'Success',
                'Item deleted successfully!',
                'Okay',
                () => {
                    window.location.href="/-V--3.0.5/model-delete/"+ pk +""
                },);
        },
        function cancelCb() {
            Notiflix.Report.failure('Failure', 'Item was saved!', 'Okay');
        },
        );
}

function confirm_product_delete(pk, inventar_number){
    var r = Notiflix.Confirm.show(
        "Warning!", 
        inventar_number + ' ' + "raqamli buyumni o'chirmoqchimisiz?", 
        "Yes", 
        "No",
        function okCb() {
            Notiflix.Report.success(
                'Success',
                'Item deleted successfully!',
                'Okay',
                () => {
                    window.location.href="/-V--3.0.5/index/base/"+ pk +"/product-delete"
                },);
        },
        function cancelCb() {
            Notiflix.Report.failure('Failure', 'Item was saved!', 'Okay');
        },
        );
}

function confirm_responsible_delete(pk, name){
    var r = Notiflix.Confirm.show(
        "Warning!", 
        name + ' ' + "ismli shaxsni o'chirmoqchimisiz?", 
        "Yes", 
        "No",
        function okCb() {
            Notiflix.Report.success(
                'Success',
                'Person deleted successfully!',
                'Okay',
                () => {
                    window.location.href="/-V--3.0.5/responsible-delete/"+ pk +""
                },);
        },
        function cancelCb() {
            Notiflix.Report.failure('Failure', 'Person was saved!', 'Okay');
        },
        );
}

function confirm_search_delete(pk){
    var r = confirm("Ushbu buyumni o'chirmoqchimisiz?");
    if (r == true) {
        window.location.href="/-V--3.0.5/index/base/"+ pk +"/product-delete"
    }
}
