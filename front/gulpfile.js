const {series,src, dest, parallel, watch} = require('gulp');
var cssnano = require('gulp-cssnano');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var imagemin = require('gulp-imagemin');
var bs = require('browser-sync').create();
var util = require('gulp-util');
var sass = require('gulp-sass');

//此处使用的是ruby+gem，安装sass，且在npm安装npm install gulp-ruby-sass
// var sass = require('gulp-ruby-sass');
var sourcemaps = require('gulp-sourcemaps');

function greet(){
	console.log('hallo word!');
}

var path = {
    'html':'./templates/**/',
    'css':'./source/css/**/*.scss',
    'js':'./source/js/',
    'images':'./source/images/',
    'css_district':'./district/css/',
    'js_district':'./district/js/',
    'images_district':'./district/images/'
};

// 未加也可以.pipe(bs.stream())

// html处理
function html(){
    return src(path.html+'*.html')
        .pipe(bs.stream())
}

// .
// src(path.css + '*.sass')
//         .pipe(sass().on('error',sass.logError))
// sass(path.css+'*.scss').on("error",sass.logError)
function css(){
    return src(path.css)
        .pipe(sass().on('error',sass.logError))
        .pipe(cssnano())
        .pipe(rename({'suffix':'.min'}))
        .pipe(dest(path.css_district))
        .pipe(bs.stream())
}





function js(){
    return src(path.js+'*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify().on('error',util.log))
        .pipe(rename({'suffix':'.min'}))
        .pipe(sourcemaps.write())
        .pipe(dest(path.js_district))
        .pipe(bs.stream())
}



// 图片处理
function images(){
    return src(path.images+'*.*')
        .pipe(cache(imagemin()))
        .pipe(dest(path.images_district))
}



//
function task(){
    js();
    css();
    html();
}
//监听
const watcher = watch([path.html+'*.html',path.js+'*.js',path.css,path.images+'*.*']);

watcher.on('change',function(paths,stats){
    console.log(`File ${paths} was add`);
    console.log('path:',paths);
    task();
});
watcher.on('add',function(path,stats){
    console.log(`File ${path} was add`);
    task();
});


watcher.on('unlink',function(path,stats){
    console.log(`File ${path} was remove`);
    task();
});

// gulp.task('watch',function(){
//     console.log('watch');
//     gulp.watch(path.html+'*.html',['html']);
//     gulp.watch(path.css+'*.scss',['css']);
//     gulp.watch(path.js+'*.js',['js']);
//     gulp.watch(path.images+'*.*',['images']);
// });

// initial 浏览器同步,// 加载bs:
// gulp.task('bs',function(){
//     bs.init({
//         'server':{'baseDir':'./'}
//     });
// });

// 换一个
function bs_event(){
    bs.init({
        'proxy':'http://127.0.0.1:8000/'
    });
}
//
//
// // 循环任务
// gulp.task('default',['bs','watch']);

exports.default = series(bs_event,parallel(
    html,
    css,
    js
));