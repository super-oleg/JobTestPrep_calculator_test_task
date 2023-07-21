const { createApp, ref } = Vue

createApp({
  setup() {
    const left = ref(0)
    const right = ref(0)
    const operator = ref('+')
    const operators = ref(['+', '-', '*', '/'])
    const result = ref(0)

    function calculate() {
      axios.post("/calculate", {
        left: left.value,
        right: right.value,
        operator: operator.value
      }).then(function (response) {
        result.value = response.data.result
      }).catch(function (error) {
        console.log(error.response)
        alert(error.response.data.error)
        })
    }

    return {
      left,
      right,
      operator,
      operators,
      result,
      calculate
    }
  }
}).mount('#app')