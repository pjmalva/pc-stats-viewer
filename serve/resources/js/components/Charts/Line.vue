<template>
  <div class="row">
    <div v-if="title" class="col-3">
      <h1><b>{{ title}}</b></h1>
    </div>
    <div :class=" title ? 'col-9':'col-12'">
      <div class="progress" style="height:50px">
        <div
          class="progress-bar progress-bar-animated progress-bar-striped"
          :style="{
            'width': percent + '%',
            'background-color': currentColor.color
          }"
        ></div>
      </div>
    </div>
    <div class="col-12 text-center mt-2">
      <h4 class="mb-0"><b>{{ percent }}%</b></h4>
      <p class="mb-0">{{ text }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      required: false
    },
    percent: {
      required: true
    },
    text: {
      default: ''
    },
    colors: {
      default: () => [
        {
          value: 0,
          color: "blue"
        },
        {
          value: 50,
          color: 'yellow',
        },
        {
          value: 70,
          color: 'orange',
        },
        {
          value: 90,
          color: 'red',
        },
      ]
    }
  },
  computed: {
    currentColor: function () {
      let color
      this.colors.forEach(element => {
        if( this.percent >= element.value ) {
          color = element
        }
      });
      return color
    }
  }
}
</script>
