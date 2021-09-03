var app = new Vue({
  el: '#app',
  data: {
    medias: ['hoge', 'fuga']
  }
})


Vue.component('todo-item', {
  template: '<li>Đây là một đề mục todo</li>'
})