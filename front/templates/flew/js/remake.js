function News(){
    this.loadMorBtnMS = $("#load-more-BTN");
}



News.prototype.listenMoreNewsBtnMs = function(){
    var self = this;
    var pages = 1;
    var load_btn1 = $('#load-more-BTN');
    var load_btn2 = $('#load-more-BTN-2');
    console.log('跑过来');
    self.loadMorBtnMS.click(function(event){
        console.log("1");
        event.preventDefault();
        console.log('2');
        yourajax.get({
            'url':'/news/news_list',
            'data':{'p':pages},
            'success':function(result){
                if (result['code'] === 200){
                    console.log('data.message',result.data.news);
                    console.log('data.message',result.data.news);
                    var datas = result['data']['news'];
                    var temp = template('template_each',{'newses':datas});
                    console.log('跑temp',datas);
                    //listUrls要放在ajax中获取才有效
                    var listUrls = $('.list-inner-group');
                    listUrls.append(temp);
                    pages += 1;
                    if (datas <= 0){
                        load_btn1.hide();
                        load_btn2.show();
                    }
                }
            }
        })
    })
};

News.prototype.Run = function(){
    this.listenMoreNewsBtnMs();
};


$(function(){
    var news = new News();
    news.Run()
});