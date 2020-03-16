import { Pie } from 'vue-chartjs'

export default {
  props: {
    usage: {
      type: Number,
      default: 0
    }
  },
  extends: Pie,
  mounted () {
    this.renderChart({
      labels: ['Usado', 'Livre'],
      datasets: [
        {
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
          ],
          data: [this.usage, 100 - this.usage]
        }
      ]
    },
    {
      responsive: true,
      maintainAspectRatio: false
    })
  }
}
