//API KEY = c243bf8af1c20f038f6724dc2891c4db

/*
NOWPLAYING 
https://api.themoviedb.org/3/movie/now_playing?api_key=<<api_key>>&language=en-US&page=1
*/

/* 
MOVIE
https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
*/

/*
    $rootScope -> created by my-app, global.
    $scope -> created by controller, current controller and its' children.
*/

var app = angular.module('aMovieApp', ['ngRoute']);

app.config(function($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
            templateUrl: 'login.html',
            controller: 'loginCtrl'          
        })

        .when('/nowplaying',{
            resolve:{
                "check": function($location, $rootScope){
                    if(!$rootScope.hasLogged){
                        alert("Please Log In first!");
                        $location.path("/");
                    }
                }
            },
            templateUrl: 'mockup_2_nowplaying.html',
            controller: 'dataTable'
        })

        .when('/details', {
            resolve:{
                "check": function($location, $rootScope){
                    if(!$rootScope.hasLogged){
                        alert("Please Log In first!");
                        $location.path("/");
                    }
                }
            },
            templateUrl: 'mockup_2_details.html',
            controller: 'dataDetail'
        })

        .when('/aboutme',{
            resolve:{
                "check": function($location, $rootScope){
                    if(!$rootScope.hasLogged){
                        alert("Please Log In first!");
                        $location.path("/");
                    }
                }
            },
            templateUrl: 'aboutme.html',
            controller: 'aboutMe'
        })
        
        .when('/logout',{
            templateUrl: 'login.html',
            controller: 'logoutCtrl'
        });
        
        //untuk menghilangkan tanda # di url
        $locationProvider.html5Mode(true);
});

app.controller('dataTable', function($scope, $http, $rootScope, $location){
    $http.get("https://api.themoviedb.org/3/movie/now_playing?api_key=c243bf8af1c20f038f6724dc2891c4db&language=en-US&page=1").then(function (response){
        $scope.moviesLi = response.data.results;

    }, function(response){
        console.log("Request can't be made at the moment");
    });

    $scope.getMoviesDetail = function(id){
        $rootScope.movieID = 'https://api.themoviedb.org/3/movie/' + id + '?api_key=c243bf8af1c20f038f6724dc2891c4db&language=en-US';
        $location.path('/details');
    }
});

app.controller('loginCtrl', function($scope, $location, $rootScope){
    sessionStorage.setItem('username', 'user');
    sessionStorage.setItem('passwords', 'uaspti');

    $scope.authorising = function(){
        if ($scope.username == sessionStorage.getItem('username') && $scope.password == sessionStorage.getItem('passwords')){
            $location.path('/nowplaying');
            $rootScope.hasLogged = true;
        } else{
            alert("Wrong combination of Username and/or Password");
        }
    }
});

app.controller('dataDetail', function($scope, $http, $rootScope, $location){
    $http.get($rootScope.movieID).then(function(response){
        $scope.movieDetails = response.data;
    },function(){
        console.log("Request can't be made at the moment");
    });

    $scope.returnBack = function(){
        $location.path('/nowplaying');
    }
});

app.controller('aboutMe', function($scope){
});

app.controller('logoutCtrl', function($scope, $location, $rootScope){
    $rootScope.hasLogged = false;
    $location.path('/');
    sessionStorage.removeItem('username');
    sessionStorage.removeItem('passwords');
    sessionStorage.clear();
});