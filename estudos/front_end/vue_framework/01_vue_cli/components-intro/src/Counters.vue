<template>

    <div class="counters">
        <app-counter v-for='c in 5' :key="c"/>
    </div>

</template>

<script>
import counterButton from './counterButton.vue'

export default {
    components: {'app-counter': counterButton }
}
</script>

<style>

</style>