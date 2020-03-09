function Course(){
    this.InputBtn = $('.InputBtn');
    this.video_photo_btn = $('#thumbnail-btn');
    this.picture_thumbnail = $('#picture-for-thumbnail');

}


Course.prototype.videoUploadEvent = function(){
    var self = this;
    self.video_input = $('#video-input');
    self.videoBTN = $('#video-BTN');
    self.pictureEvent(self.videoBTN,self.video_input)
};

Course.prototype.uploadImageEvent = function(){
    var self = this;
    self.pictureEvent(self.video_photo_btn,self.picture_thumbnail)
};

//上传视频缩略图函数
Course.prototype.pictureEvent = function(btn,input_val){
    var self = this;
    console.log('发布电影中1');
    btn.change(function(){
        var file = btn[0].files[0];
        var form = new FormData();
        form.append('file',file);
        yourajax.post({
            "url":"/course/course_upload_picture",
            "data":form,
            "contentType":false,
            "processData":false,
            "success":function(event){
                if (event["code"] === 200){
                    var url = event["data"]["url"];
                    input_val.val(url);
                }
            }

        })
    })
};




Course.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor",{
        'serverUrl': '/ueditor/upload/'
    });
};

Course.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function () {
        var title = $("#title-input").val();
        var category_id = $("#category-input").val();
        var teacher_id = $("#teacher-input").val();
        var video_url = $("#video-input").val();
        var cover_url = $("#picture-for-thumbnail").val();
        var price = $("#price-input").val();
        var duration = $("#duration-input").val();
        var profile = window.ue.getContent();

        yourajax.post({
            'url': '/cms/course_cms_add',
            'data': {
                'title': title,
                'video_url': video_url,
                'cover_url': cover_url,
                'price': price,
                'duration': duration,
                'profile': profile,
                'category_id': category_id,
                'teacher_id': teacher_id
            },
            'success': function (result) {
                if(result['code'] === 200){
                    window.location = window.location.href;
                }
            }
        });
    });
};


Course.prototype.listenInputEvent = function(){
    var self = this;
    document.getElementById("InputBtn").addEventListener("input", myFunction);
    function myFunction() {
        console.log('input event change')
    }
};

Course.prototype.consoleEvent = function(){
    console.log('input event change')
};

Course.prototype.Run = function(){
    this.initUEditor();
    this.listenSubmitEvent();
    // this.pictureEvent();
    this.uploadImageEvent();
    this.videoUploadEvent();
};




$(function(){
    var course = new Course();
    course.Run();
});