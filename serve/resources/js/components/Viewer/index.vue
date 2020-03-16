<template>
  <div class="col-12 p-0 m-0">
    <status :status="items" />
  </div>
</template>

<script>
import Status from './../Status'
export default {
  components: {
    status: Status
  },
  data() {
    return {
      items: {}
    }
  },
  methods: {
    loadData: function () {
      axios.get('/api/info/get',{
        params: {
          listit: 1
        }
      }
      )
        .then( res => {
          this.items = res.data.data
        })
        .catch( err => {
          console.error( err )
        })
    },
    listStateClockUpdateStart: function () {
      setInterval(
        this.loadData(), 5 * 1000
      )
    }
  },
  mounted() {
    this.listStateClockUpdateStart()
  }
}
</script>

<style>

</style>
