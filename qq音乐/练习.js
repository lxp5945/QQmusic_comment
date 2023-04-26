function c(){
                        var arr=[].slice.call(arguments);   // 这里的[].slice实际就是一个函数
                        console.log(arguments);
                        console.log(arr);
        };
                    c(1,2,333);
var person = {
  firstName  : "John",
  lastName   : "Doe",
  id         : 5566,
  myFunction : function() {
    return this;
  }
};
console.log(person.myFunction)

