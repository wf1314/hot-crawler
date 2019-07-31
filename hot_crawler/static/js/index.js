function main() {
    $.ajax({
    url: "/api/v1_0/zhihu",
    type: "GET",
    dataType: "json",
    success: function(data) {
        var title, excerpt, metrics, link, image;

        if (data.code == 0){
            for ( i=0; i<data.data.length; i++) {
                title = data.data[i].title;
                excerpt = data.data[i].excerpt;
                metrics = data.data[i].metrics;
                link = data.data[i].link;
                image = data.data[i].image;
                $("body").append("<div>"+ i + '.' + title + "</div>");
            }
        }else{
            console.log(data.msg)
        }
    }
});
}

main();