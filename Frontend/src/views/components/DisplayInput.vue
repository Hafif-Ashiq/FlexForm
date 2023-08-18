<template >
    <div class="main-div" >
        
        <div v-if="input_type === 'text' || input_type === 'email' || input_type === 'password' || input_type === 'number' "  >
            <label for="in" class="input-label">Text Field Placeholder</label>
            <input spellcheck= 'false' type="text" name="in" class="input"  placeholder="Answer Placeholder" v-model="placeholder">
        </div>
        <input v-else-if=" input_type === 'date' || input_type === 'file'" disabled
            :type="input_type" class="input" :placeholder="input_type.toUpperCase()">
            <div class="textarea-div"  v-else-if="input_type === 'textarea'">
                <textarea disabled name="" id="" cols="30" rows="20" class="textarea-input" ></textarea>

            </div>
            <div v-else-if="input_type === 'multiplechoice' || input_type === 'checkbox' || input_type === 'radio' || input_type === 'dropdown'">
            <form @submit.prevent="addOptions" >
                <label for="placeholder" class="input-label">Enter the different options</label>
                <input spellcheck= 'false' type="text" v-model="optionText" class="input" placeholder="Enter option">
            </form>
            <div v-if="options.length !== 0"  class="options-div" >
                <div v-for="(option,index) in options" :key="index" @click="deleteOption(index)" class="option-group bg-gradient-info" >
                    <p  class="option " >{{ option }}</p>
                    <img :src="cross" class="cross"  alt="">
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import cross from "../../assets/icons/cross.svg"
export default {
    props:['input_type','input_data'],
    data() {
        return {
            
            placeholder : '',
            options: [],
            optionText: "",
            cross
        }
    },
    mounted(){
        if (this.input_data) {
            if (this.input_data['placeholder'] != null) {
                this.placeholder = this.input_data['placeholder']
            }
            if (this.input_data['options'] != null) {
                this.options = this.input_data['options']

            }
        }
    },
    
    watch:{
        placeholder(){
            this.handleChange()
        },
        options(){
            this.handleChange()
        },
        input_data(){

            if (this.input_data['placeholder'] != null) {
                this.placeholder = this.input_data['placeholder']
            }
            if (this.input_data['options'] != null) {
                this.options = this.input_data['options']

            }
            
            this.handleChange()
        }
    },
    
   
    methods: {
        addOptions() {
            if (this.optionText !== '') {
                this.options.push(this.optionText)
                this.optionText = ""

                this.handleChange()
            }
        },
        deleteOption(index){
            this.options.splice(index, 1)
        },
        handleChange(){
            const data = {}
            if (this.input_type === 'text' || this.input_type === 'email' || this.input_type === 'number' || this.input_type === 'password') {
                data['placeholder'] = this.placeholder
                data['options'] = null
            }
            else if (this.input_type === 'multiplechoice' || this.input_type === 'checkbox' || this.input_type === 'radio' || this.input_type === 'dropdown') {
                data['options'] = this.options
                data['placeholder'] = null
            }
            else{
                data['options'] = null
                data['placeholder'] = null
            }
            this.$emit('change-data',data)
        }
    }
}
</script>
<style scoped>

.input{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 20px 20px;

    height: 75px;
    border-radius: 14px;
    border: 1px solid #b6b6b6;
    /* border: none; */
    font-weight: 600;
    font-size: 17px;
    /* color: #dfdfdf; */
    background-color: #f8f9fa;
    /* cursor: pointer; */
    user-select: none;
    /* box-shadow: -1px 1px 3px 0px gray; */
    
}

.textarea-input{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    /* padding: 10px 20px; */
    height: 165px;
    border-radius: 14px;
    border: 1px solid #b6b6b6;
    resize: none;
    font-size: 16px;
    background-color: #f8f9fa;
    user-select: none;
    

}
.input:focus{
    outline: none;  
}

.input-label{
    font-size: 16px;
}

.options-div{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    padding: 15px 10px;
    gap: 15px;
    align-items: center ;
    justify-content: start;
    position: relative;
    z-index: 0;
}

.option{
    /* background: #217cff; */
    margin: unset;

}
.option-group{
    display: flex;
    position: relative;
    padding: 10px 20px;
    color: white;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    transition: all 200ms ease-out;
    cursor: pointer;
}


.cross{
    position: absolute; 
    top: 50%;
    left: 50%;
    width: 35px;
    height: 35px;

    opacity: 0;


    translate: -50% -50%;
}


.option-group:hover {
    .cross{
        opacity: 1;
    }
    .option{
        opacity: 0;
    }

}



</style>