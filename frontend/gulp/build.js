'use strict';

var gulp = require('gulp');
var gulpif = require('gulp-if');
var debug = require('gulp-debug');

var paths = gulp.paths;

var do_uglyfy = true;
var do_minify_partials = False;
var do_minify_partials_htmlmin = true;
var do_minify_html_htmlmin = true;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('partials', ['markups'], function() {
  return gulp.src([
    paths.src + '/{app,components,services,modules}/**/*.html',
    paths.tmp + '/{app,components,services,modules}/**/*.html'
  ])
    .pipe(gulpif(do_minify_partials, $.minifyHtml({
      empty: true, // KEEP empty attributes
      spare: true, // KEEP redundant attributes
      quotes: true, // KEEP redundant attributes
      loose: true // KEEP one whitespace (needed for angular-gettext)
    })))
    .pipe(gulpif(do_minify_partials_htmlmin, $.htmlmin({
      removeComments: true
    })))
    .pipe($.angularTemplatecache('templateCacheHtml.js', {
      module: 'squirrel'
    }))
    .pipe(gulp.dest(paths.tmp + '/partials/'));
});

gulp.task('html', ['inject', 'partials', 'pot', 'translations'], function() {
  var partialsInjectFile = gulp.src(paths.tmp + '/partials/templateCacheHtml.js', {
    read: false
  });
  var partialsInjectOptions = {
    starttag: '<!-- inject:partials -->',
    ignorePath: paths.tmp + '/partials',
    addRootSlash: false
  };

  var htmlFilter = $.filter('*.html');
  var jsFilter = $.filter('**/*.js');
  var cssFilter = $.filter('**/*.css');
  var assets;

  return gulp.src(paths.tmp + '/serve/*.html')
    .pipe($.inject(partialsInjectFile, partialsInjectOptions))
    .pipe(assets = $.useref.assets())
    .pipe($.rev())
    .pipe(jsFilter)
    .pipe(debug({
      title: 'copying js:'
    }))
    .pipe($.replace('MODE: "dev"', 'MODE: "prod"'))
    .pipe($.ngAnnotate())
    .pipe(gulpif(do_uglyfy, $.uglify({
      preserveComments: $.uglifySaveLicense
    })))
    .pipe(jsFilter.restore())
    .pipe(cssFilter)
    .pipe(debug({
      title: 'copying css from:'
    }))
    .pipe($.replace('../bootstrap/fonts', 'fonts'))
    .pipe($.replace('../bower_components/font-awesome', 'fonts/'))
    .pipe($.replace('/bower_components/bootstrap/fonts', '/fonts'))
    .pipe($.replace('./fonts/slick', '/fonts/slick'))
    .pipe($.replace('./ajax-loader.gif', '/assets/images/ajax-loader.gif'))
    .pipe(gulpif(do_uglyfy, $.csso()))
    .pipe(cssFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe(htmlFilter)
    .pipe(debug({
      title: 'copying html:'
    }))
    .pipe(gulpif(do_minify_partials, $.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    })))
    .pipe(gulpif(do_minify_html_htmlmin, $.htmlmin({
      removeComments: true
    })))
    .pipe($.htmlPrettify({
      indent_char: ' ',
      indent_size: 2
    }))
    .pipe(htmlFilter.restore())
    .pipe(gulp.dest(paths.dist + '/'))
    .pipe($.size({
      title: paths.dist + '/',
      showFiles: true
    }));
});

gulp.task('images', function() {
  return gulp.src(paths.src + '/assets/images/**/*')
    .pipe(debug({
      title: 'copying image:'
    }))
    .pipe(gulp.dest(paths.dist + '/assets/images/'));
});

gulp.task('fonts', function() {
  return gulp.src($.mainBowerFiles())
    /*.pipe(debug({
      title: 'copying main bower file:'
    }))*/
    .pipe($.filter('**/*.{eot,svg,ttf,woff,woff2}'))
    .pipe(debug({
      title: 'copying font:'
    }))
    .pipe($.flatten())
    .pipe(gulp.dest(paths.dist + '/fonts/'));
});

gulp.task('misc', function() {
  return gulp.src(paths.src + '/**/*.{ico,png}')
    .pipe(debug({
      title: 'copying ico:'
    }))
    .pipe(gulp.dest(paths.dist + '/'));
});

gulp.task('clean', function(done) {
  $.del([paths.dist + '/', paths.tmp + '/'], done);
});

gulp.task('build', ['html', 'images', 'fonts', 'misc']);
