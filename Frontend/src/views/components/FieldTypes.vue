<template >
    <div class="question-types">
        <div v-for="(field,index) in fields" class="type" :key="field['name']" @click="handleSelect(index)" :style="{'background-color':field['fill']}">
            <img :src="field['icon']"  alt="">
            <h5>{{ field['name'] }}</h5>
        </div>
    </div>
</template>
<script>

export default {
    props: ['fields'],
    data(){
        return{
            
        }
    },
    methods:{
        handleSelect(type){
            this.$emit('select',type)
        }
    }
}
</script>
<style scoped>
    .question-types{
        width: 800px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 10px;
        padding: 20px;
        background-color: white;
        position: absolute;
        top: 100%;
        left: 0%;
        z-index: 10;
        border-radius: 20px;
        box-shadow: -1px 1px 12px 2px rgb(212, 212, 212);
    }
    .type{
        display: flex;
        flex-direction: row;
        justify-content: start;
        align-items: center;
        padding: 10px 20px;
        height: 50px;
        gap:8px ;
        width: 100%;
        border-radius: 12px;
        cursor: pointer;
    }
    .type h5{
        padding: 0px;
        margin: 0px;
    }

    
</style>