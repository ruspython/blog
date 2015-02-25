/*global module:false*/
module.exports = function (grunt) {

    grunt.initConfig({
        // Metadata.
        pkg: grunt.file.readJSON('package.json'),
        banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
        '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
        '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
        '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
        ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
        // Task configuration.

        copy: {
            images: {
                expand: true,
                cwd: 'assets/images/',
                src: '**',
                dest: 'blog/static/img/'
            },
            fonts: {
                expand: true,
                cwd: 'assets/fonts/',
                src: '**',
                dest: 'blog/static/fonts/'
            }
        },
        less: {
            development: {
                options: {
                    compress: false
                },
                files: {
                    'blog/static/css/portfolio/style.css': 'assets/less/portfolio/style.less',
                    'blog/static/css/style.css': 'assets/less/style.less'
                }
            }
        },
        cssmin: {
            options: {
                banner: '/*! <%= pkg.name %> v<%= pkg.version %>, <%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            combine: {
                files: {
                    'blog/static/css/style.css': [
                        'blog/static/css/style.css'
                    ]
                }
            }
        },
        concat: {
            options: {},
            js: {
                src: [
                    'bower_components/jquery/dist/jquery.js'

                ],
                dest: 'blog/static/js/script.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> v<%= pkg.version %>, <%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            build: {
                src: 'blog/static/js/script.js',
                dest: 'blog/static/js/script.js'
            },
            pages: {
                expand: true,
                cwd: 'assets/js/pages/',
                src: '*.js',
                dest: 'blog/static/js/'
            }
        },
        watch: {
            less: {
                files: 'assets/less/**/*.less',
                tasks: ['less'] //, 'cssmin'
            },
            js: {
                files: 'assets/js/**/*.js',
                tasks: ['concat']
            },
            images: {
                files: 'assets/images/**/*',
                tasks: ['copy:images']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-copy');


    grunt.registerTask('default', ['copy', 'less', 'cssmin', 'coffee', 'concat', 'watch']);
    grunt.registerTask('build', ['copy', 'less', 'cssmin', 'coffee', 'concat', 'uglify']);

};

