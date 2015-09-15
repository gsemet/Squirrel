'use strict';

var path = require('path');
var gulp = require('gulp');
var conf = require('./conf');

var browserSync = require('browser-sync');

var $ = require('gulp-load-plugins')();

var wiredep = require('wiredep').stream;
var _ = require('lodash');

gulp.task('styles', function() {
  var lessOptions = {
    options: [
      'bower_components',
      path.join(conf.paths.src, '/app'),
      path.join(conf.paths.src, '/modules')
    ]
  };

  var injectFiles = gulp.src([
    path.join(conf.paths.src, '/app/**/*.less'),
    path.join(conf.paths.src, '/modules/**/*.less'),
    path.join('!' + conf.paths.src, '/app/index.less'),
    path.join('!' + conf.paths.src, '/app/vendor.less')
  ], {
    read: false
  });

  var injectOptions = {
    transform: function(filePath) {
      filePath = filePath.replace(conf.paths.src + '/app/', '');
      filePath = filePath.replace(conf.paths.src + '/modules/', '');
      return '@import "' + filePath + '";';
    },
    starttag: '// injector',
    endtag: '// endinjector',
    addRootSlash: false
  };


  return gulp.src([
    path.join(conf.paths.src, '/app/index.less'),
    path.join(conf.paths.src, '/app/vendor.less')
  ])
    .pipe($.inject(injectFiles, injectOptions))
    .pipe(wiredep(_.extend({}, conf.wiredep)))
    .pipe($.sourcemaps.init())
    .pipe($.less(lessOptions)).on('error', conf.errorHandler('Less'))
    .pipe($.autoprefixer()).on('error', conf.errorHandler('Autoprefixer'))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest(path.join(conf.paths.tmp, '/serve/app/')))
    .pipe(browserSync.reload({
      stream: true 
    }));
});
