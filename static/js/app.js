/**
 * Created by ASUS on 012 12.06.16.
 */
var app = angular.module('startpage', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller('DemoCtrl', function DemoCtrl($scope, $log, $http) {
        $scope.loadItems = function () {
            $http({
                method: 'GET',
                url: '/api/shopping'
            }).then(function successCallback(data) {
                $scope.items = data;
                console.log(data)
            }, function errorCallback(data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
        };

        $scope.loadItems();

        //$scope.saveItem = function()
    }
);


//startpage.controller('DemoCtrl', ['$scope', function($scope) {
//    $scope.num = 0;
//    $scope.save = function() {
//        $(".data").html("Click "+$scope.num);
//        $scope.num += 1;
//    }
//}
//]);