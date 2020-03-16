<template>
  <div class="row p-0 m-0">
    <div class="col-12 py-5 d-flex justify-content-between bg-dark">
      <div>
        <img v-if="status.company.logo" :src="`/storage/img/${status.company.logo}`" height="100">
        <h1 class="text-white" :style="{
          'color': status.company.color ? status.company.color : '#000'
        }">
          <b class="text-uppercase">{{ status.server.name }}</b> <small>({{ status.company.name }})</small>
        </h1>
      </div>

      <h5 class="text-white-50">
        Ultima atualização: {{ status.server.last_update }}
        <br>
        Ciclo: {{ status.server.interval }} minuto(s)
      </h5>
    </div>

    <div
      class="clearfix col-12 mb-4"
      :style="{
        'height': '20px',
        'background-color': status.company.logo ? status.company.logo : 'green'
      }"
    ></div>


    <div v-if="status.company.obs" class="col-12">
      <h4>Observações</h4>
      <p v-html="status.company.obs"></p>
    </div>

    <div class="col-12 col-md-6 col-lg-4 mb-3" v-if="status.cpu">
      <!-- <h4>Uso da CPU:</h4> -->
      <line-chart
        title="CPU"
        :percent="status.cpu"
      />
    </div>

    <div class="col-12 col-md-6 col-lg-4 mb-3" v-if="status.memory">
      <!-- <h4 class="card-title">Uso da Memória:</h4> -->
      <line-chart
        title="RAM"
        :percent="status.memory.percent"
        :text="`${ convertBToGB( status.memory.available) } GB disponiveis`"
      />
    </div>

    <div class="col-12 col-md-6 col-lg-4  mb-3" v-if="status.disk">
      <!-- <h4 class="card-title">Uso de Disco:</h4> -->
      <line-chart
        v-for="disk,i in status.disk"
        :key="i"
        :title="`${ disk.disk }`"
        :percent="disk.percent"
        :text="`${ convertBToGB( disk.free) } GB disponiveis`"
      />
    </div>

    <div class="col-12 col-md-6 mb-3" v-if="status.network">
      <h4 class="card-title">Atividade de Rede:</h4>

      <div class="row d-flex justify-content-center">
        <div class="card">
          <div class="card-body">
            <p class="mb-0"><small>ENVIADOS</small></p>
            <h4><b>{{ convertBToMB(status.network.send) }}<small>Mb</small></b></h4>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <p class="mb-0"><small>RECEBIDOS</small></p>
            <h4><b>{{ convertBToMB(status.network.recv) }}<small>Mb</small></b></h4>
          </div>
        </div>
      </div>
      <div class="list-group">
        <div
          class="list-group-item d-flex justify-content-between"
          v-for="ip,i in status.network.ipaddrs"
          :key="i"
        >
          <h3><b>{{ i }}</b></h3>
          <div>
            <div class="text-right" v-for="addrs,i in ip">{{ addrs[1] }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="col-12 col-md-6 mb-3" v-if="status.proccess">
      <h4 class="card-title">Processos Ativos:</h4>

      <div class="row px-3">
        <div
          class="card col-12 col-md-6 col-lg-3 p-0"
          v-for="proccess in status.proccess.most_memory.slice(0,12)"
          :key="proccess.id"
        >
          <div class="card-header p-1 m-0">
            {{ proccess.name }} <small><b>({{ proccess.id }})</b></small>
          </div>
          <div class="card-body p-1 m-0">
            <!-- <p class="mb-0">PID: {{ proccess.id }}</p> -->
            <p class="mb-0">Memória: <b>{{ proccess.memory.toFixed(2) }}%</b></p>
            <p class="mb-0">Usuário: <b>{{ proccess.user }}</b></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MemoryUsage from './../Charts/MemoryUsage'
import CpuUsage from './../Charts/CpuUsage'
import DiskUsage from './../Charts/DiskUsage'

import LineChart from './../Charts/Line'

export default {
  props: {
    status: {
      required: true
    }
  },
  components: {
    "memory-usage": MemoryUsage,
    "cpu-usage": CpuUsage,
    "disk-usage": DiskUsage,
    "line-chart": LineChart
  },
  methods: {
    convertBToGB (bytes) {
      return ((((bytes)/1024)/1024)/1024).toFixed(2)
    },
    convertBToMB (bytes) {
      return (((bytes)/1024)/1024).toFixed(2)
    }
  }
}
</script>

<style>

</style>
