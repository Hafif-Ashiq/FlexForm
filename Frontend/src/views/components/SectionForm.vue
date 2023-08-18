<template >
            <div class="section-complete" >

<div class="heading-div shadow " :style="sect_color === ''? {'backgroundColor' : '#2152ff'} : {'backgroundColor' : sect_color}">
    <div class="section-details ">
        <p class="section-num font-white">{{ indexSect + 1 }} of {{ totalSects }}</p>
        <input spellcheck= 'false' type="text" class="input font-white heading-input" v-model="sectionTitle"
            placeholder="Section Title ">
    </div>
    
    <div class="section-actions">
        <!-- drag -->
        <svg width="42" height="42" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
            <g fill="none" fill-rule="evenodd">
                <rect transform="rotate(-180 17 17)" width="34" height="34" rx="14" />
                <g transform="rotate(-180 12 11)" fill="#fff" stroke="#fff" stroke-width="1.5">
                    <ellipse cx="2.059" cy="2.083" rx="1.647" ry="1.672" />
                    <ellipse cx="2.059" cy="7.917" rx="1.647" ry="1.672" />
                    <ellipse cx="7" cy="2.083" rx="1.647" ry="1.672" />
                    <ellipse cx="7" cy="7.917" rx="1.647" ry="1.672" />
                    <ellipse cx="11.941" cy="2.083" rx="1.647" ry="1.672" />
                    <ellipse cx="11.941" cy="7.917" rx="1.647" ry="1.672" />
                </g>
            </g>
        </svg>
        <!-- copy  -->
        <svg @click="copySection" width="42" height="42" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
            <g fill="none" fill-rule="evenodd">
                <rect width="42" height="42" rx="14" />
                <path d="M5 5h24v24H5z" />
                <path
                    d="M20.188 9a2.99 2.99 0 0 1 2.12.879 2.99 2.99 0 0 1 .88 2.121v6a2.99 2.99 0 0 1-.88 2.121 2.99 2.99 0 0 1-2.12.879h-3.375a2.99 2.99 0 0 1-2.122-.879A2.99 2.99 0 0 1 13.812 18v-6c0-.828.336-1.578.88-2.121A2.99 2.99 0 0 1 16.811 9z"
                    stroke="#fff" stroke-width="2" />
                <path d="M10 15v4a6 6 0 0 0 6 6h3" stroke="#fff" stroke-width="1.846" stroke-linecap="round"
                    stroke-linejoin="round" />
            </g>
        </svg>
        <!-- color -->
        <div class="color-div">
            <input type="color"   class="colorinput" v-model="sect_color">
            <svg width="42" height="42" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
                <g fill="none" fill-rule="evenodd">
                    <rect fill-opacity=".14" fill="#FFF" width="34" height="34" rx="14" />
                    <path d="M6 6h22v22H6z" />
                    <path
                        d="M17 7.833c-5.05 0-9.167 4.116-9.167 9.167 0 5.05 4.116 9.167 9.167 9.167a2.293 2.293 0 0 0 2.292-2.292c0-.56-.211-1.1-.587-1.53a.484.484 0 0 1-.12-.303c0-.257.203-.459.46-.459h1.622c3.034 0 5.5-2.465 5.5-5.5 0-4.546-4.116-8.25-9.167-8.25zm5.042 10.084c-.761 0-1.375-.614-1.375-1.375s.614-1.375 1.375-1.375c.76 0 1.375.614 1.375 1.375 0 .76-.615 1.375-1.375 1.375zm-2.75-3.667c-.761 0-1.375-.614-1.375-1.375 0-.76.614-1.375 1.375-1.375.76 0 1.375.614 1.375 1.375 0 .76-.614 1.375-1.375 1.375zm-8.709 2.292c0-.761.614-1.375 1.375-1.375s1.375.614 1.375 1.375c0 .76-.614 1.375-1.375 1.375-.76 0-1.375-.614-1.375-1.375zm5.5-3.667c0 .76-.614 1.375-1.375 1.375-.76 0-1.375-.614-1.375-1.375 0-.76.614-1.375 1.375-1.375s1.375.614 1.375 1.375z"
                        fill="#FFF" fill-rule="nonzero" />
                </g>
            </svg>
        </div>
        <!-- delete -->

        <svg @click="deleteSection" v-if="totalSects > 1" width="42" height="42" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
            <g fill="none" fill-rule="evenodd">
                <rect width="42" height="42" rx="14" />
                <path
                    d="M22 9h-1.5l-.71-.71c-.18-.18-.44-.29-.7-.29h-4.18c-.26 0-.52.11-.7.29L13.5 9H12c-.55 0-1 .45-1 1s.45 1 1 1h10c.55 0 1-.45 1-1s-.45-1-1-1zm-7 3h4a4 4 0 0 1 4 4v6a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4v-6a4 4 0 0 1 4-4z"
                    fill="#fff" fill-rule="nonzero" />
            </g>
        </svg>
    </div>
</div>
<div class="questions ">
    <div class="question shadow" v-for="(question, index) in questions" @change="handleChange" :key="index">
        <div class="top-question">
            <h4 class="font-color">{{ index + 1 }}</h4>
            <div class="toggle-div">
                <h4 class="font-color">Required</h4>
                <ToggleSwitch :value="question['isRequired']" @change-value="changeRequired(index)" />
            </div>
        </div>
        <div class="body-question">
            <div class="qname-section">
                <input type="text" spellcheck= 'false'  class="input heading-input question-input" v-model="question['question']"
                    placeholder="Your Question">
                <span></span>
            </div>
            <input type="text" spellcheck= 'false' class="input description-input" v-model="question['description']"
                placeholder="Details (Optional)">
        </div>

        <div class="type-question-div">

            <div class="type-question" @click="handleShowField(index)">
                <p class="answer-type-1" v-if="question['type'] === ''">Select Answer Type</p>
                <div class="answer-type-2" v-if="question['type'] !== ''">
                    <p>Type: </p>
                    <img :src="getFieldIcon(index)" alt="">
                    <h5>{{ getFieldName(index) }}</h5>
                </div>
                <img src="../../assets/icons/arrow-down.svg" alt="">
            </div>
            <field-types v-if="showFieldTypes === index" :fields="fields"
                @select="(field) => addInput(index, field)" />
        </div>
        <div v-if="question['type'] !== ''" class="input-question">
            <display-input :input_type="question['type']" :key="handleKey" :input_data="question['data']"
                @change-data="(data) => handleInputFieldChange(index, data)" />
        </div>

        <div class="question-icons">
            <!-- drag -->
            <svg width="34" height="34" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
                <g fill="none" fill-rule="evenodd">
                    <rect transform="rotate(-180 17 17)" width="34" height="34" rx="14" />
                    <g transform="rotate(-180 12 11)" fill="#333" stroke="#333" stroke-width=".824">
                        <ellipse cx="2.059" cy="2.083" rx="1.647" ry="1.672" />
                        <ellipse cx="2.059" cy="7.917" rx="1.647" ry="1.672" />
                        <ellipse cx="7" cy="2.083" rx="1.647" ry="1.672" />
                        <ellipse cx="7" cy="7.917" rx="1.647" ry="1.672" />
                        <ellipse cx="11.941" cy="2.083" rx="1.647" ry="1.672" />
                        <ellipse cx="11.941" cy="7.917" rx="1.647" ry="1.672" />
                    </g>
                </g>
            </svg>
            <!-- copy -->
            <svg @click="copyQuestion(index)" width="34" height="34" viewBox="0 0 34 34"
                xmlns="http://www.w3.org/2000/svg">
                <g fill="none" fill-rule="evenodd">
                    <rect width="34" height="34" rx="14" />
                    <path d="M5 5h24v24H5z" />
                    <path
                        d="M20.188 9a2.99 2.99 0 0 1 2.12.879 2.99 2.99 0 0 1 .88 2.121v6a2.99 2.99 0 0 1-.88 2.121 2.99 2.99 0 0 1-2.12.879h-3.375a2.99 2.99 0 0 1-2.122-.879A2.99 2.99 0 0 1 13.812 18v-6c0-.828.336-1.578.88-2.121A2.99 2.99 0 0 1 16.811 9z"
                        stroke="#333" stroke-width="2" />
                    <path d="M10 15v4a6 6 0 0 0 6 6h3" stroke="#333" stroke-width="1.846" stroke-linecap="round"
                        stroke-linejoin="round" />
                </g>
            </svg>
            <!-- delete -->
            <svg @click="deleteQuestion(index)" v-if="questions.length !== 1" width="34" height="34"
                viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg">
                <g fill="none" fill-rule="evenodd">
                    <rect width="34" height="34" rx="14" />
                    <path
                        d="M22 9h-1.5l-.71-.71c-.18-.18-.44-.29-.7-.29h-4.18c-.26 0-.52.11-.7.29L13.5 9H12c-.55 0-1 .45-1 1s.45 1 1 1h10c.55 0 1-.45 1-1s-.45-1-1-1zm-7 3h4a4 4 0 0 1 4 4v6a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4v-6a4 4 0 0 1 4-4z"
                        fill="#333" fill-rule="nonzero" />
                </g>
            </svg>


        </div>

    </div>
</div>
<div class="button-div">
    <button class="create-button " @click="addQuestion">
        <svg class="plus" fill="url(#myGradient)" width="800px" height="800px" viewBox="0 0 32 32"
            xmlns="http://www.w3.org/2000/svg">
            <path d="M9,17h6v6a1,1,0,0,0,2,0V17h6a1,1,0,0,0,0-2H17V9a1,1,0,0,0-2,0v6H9a1,1,0,0,0,0,2Z" />
            <defs>
                <linearGradient id="myGradient" gradientTransform="rotate(310)">
                    <stop offset="0%" stop-color="#2152ff" />
                    <stop offset="100%" stop-color="#21d4fd" />
                </linearGradient>
            </defs>
        </svg>
        <span>Add Another Question</span>
    </button>
    <button class="create-button " v-if="indexSect + 1 === totalSects" @click="addSection">
        <svg class="plus" fill="url(#myGradient)" width="800px" height="800px" viewBox="0 0 32 32"
            xmlns="http://www.w3.org/2000/svg">
            <path d="M9,17h6v6a1,1,0,0,0,2,0V17h6a1,1,0,0,0,0-2H17V9a1,1,0,0,0-2,0v6H9a1,1,0,0,0,0,2Z" />
            <defs>
                <linearGradient id="myGradient" gradientTransform="rotate(310)">
                    <stop offset="0%" stop-color="#2152ff" />
                    <stop offset="100%" stop-color="#21d4fd" />
                </linearGradient>
            </defs>
        </svg>
        <span>Create Another Section</span>
    </button>
</div>


</div>

</template>
<script>
import ToggleSwitch from '../../components/Toggle-Switch.vue';
import FieldTypes from './FieldTypes.vue';
import DisplayInput from './DisplayInput.vue';
import text from "../../assets/icons/text.svg"
import date from "../../assets/icons/date.svg"
import multiselect from "../../assets/icons/multiselect.svg"
import file from "../../assets/icons/file.svg"
import password from "../../assets/icons/password.svg"
import number from "../../assets/icons/number.svg"
import radio from "../../assets/icons/radio.svg"
import textarea from "../../assets/icons/textarea.svg"
import email from "../../assets/icons/email.svg"
import dropdown from "../../assets/icons/dropdown.svg"
import checkbox from "../../assets/icons/checkbox.svg"


export default {
    components: {
        ToggleSwitch,
        FieldTypes,
        DisplayInput,

    },
    // props:['sect_questions','title'],
    props: ['section', 'totalSects', 'indexSect'],
    mounted() {
            this.handleMounted()


    },
    watch:{
        sectionTitle(){
            this.handleChange()
        },
        sect_color(){
            this.handleChange()

        }
    },
    data() {
        return {
            key:0,
            fields: [
                {
                    name: "Text Field",
                    type: "text",
                    icon: text,
                    fill: "#FF6A4820"
                },
                {
                    name: "Date",
                    type: "date",
                    icon: date,
                    fill: "#9C69CC20"

                },
                {
                    name: "Multiple Choice",
                    type: "multiplechoice",
                    icon: multiselect,
                    fill: "#963E7820"

                },
                {
                    name: "Email Field",
                    type: "email",
                    icon: email,
                    fill: "#F8B83820"

                },
                {
                    name: "Upload File",
                    type: "file",
                    icon: file,
                    fill: "#FA7B9F20"

                },
                {
                    name: "Checkbox",
                    type: "checkbox",
                    icon: checkbox,
                    fill: "#51AFA420"

                },
                {
                    name: "Number",
                    type: "number",
                    icon: number,
                    fill: "#3EAB6820"

                },
                {
                    name: "Radio Button",
                    type: "radio",
                    icon: radio,
                    fill: "#15994720"

                },
                {
                    name: "Text Area",
                    type: "textarea",
                    icon: textarea,
                    fill: "#5883C720"

                },
                {
                    name: "Password Field",
                    type: "password",
                    icon: password,
                    fill: "#268DFF20"

                },
                {
                    name: "Dropdown",
                    type: "dropdown",
                    icon: dropdown,
                    fill: "#FF5F7220"

                },
            ],


            showFieldTypes: -1,

            showInput: false,
            typeSelected: null,

            sect: { ...this.section },

            sectionTitle: "",
            sect_color:'',

            questions: [{

            }]

        }
    },
    methods: {
        handleKey(){
            this.key += 1

            return this.key
        },
        
        handleMounted(){
            this.sectionTitle = this.section['title']

            this.sect_color = this.section['color']

                

            this.questions = this.section['questions']
            // console.log(this.indexSect + " " + this.totalSects );

        },

        addInput(index, field) {

            this.typeSelected = this.fields[field]
            this.showFieldTypes = false
            this.showInput = index
            this.questions[index]['type'] = this.fields[field]['type']


        },
        handleInputFieldChange(index, value) {

            this.questions[index]['data'] = value
            
        },
        handleShowField(index) {

            if (this.showFieldTypes === index) {
                this.showFieldTypes = -1
                return
            }
            else {
                this.showFieldTypes = index
            }
        },
        changeRequired(index) {

            this.questions[index]['isRequired'] = !this.questions[index]['isRequired']

        }
        ,
        getFieldIcon(index) {
            for (let i = 0; i < this.fields.length; i++) {
                if (this.questions[index]['type'] === this.fields[i]['type']) {
                    return this.fields[i]['icon']
                }

            }
        },
        getFieldName(index) {
            for (let i = 0; i < this.fields.length; i++) {
                if (this.questions[index]['type'] === this.fields[i]['type']) {
                    return this.fields[i]['name']
                }

            }
        },
        addQuestion() {
            this.questions.push({

                isRequired: false,
                question: "",
                description: "",
                type: '',
                data: {},
            })
        },
        addSection() {
            this.$emit('add-section')
        },
        handleChange() {
            const data = {
                'title': this.sectionTitle,
                'color' : this.sect_color,
                'questions': this.questions
            }

            this.$emit('data-changed', data)
        },


        deleteQuestion(index) {

            this.questions.splice(index, 1)
        },

        copyQuestion(index) {
            this.questions.push({

                isRequired: this.questions[index]['isRequired'],
                question: this.questions[index]['question'],
                description: this.questions[index]['description'],
                type: this.questions[index]['type'],
                data: this.questions[index]['data'],
            })
        },

        copySection(){
            this.$emit('copy-section')
        },
        deleteSection(){

            this.$emit('delete-section')
            
        }
    }
}
</script>
<style scoped>
.section-complete {
    display: flex;
    flex-direction: column;
    gap: 30px;


}

.font-color {
    color: #141727;
}

.font-white {
    color: white;
}

p {
    margin: 0;
    padding: 0;
    font-weight: 600;

}

.input {
    border: none;
    background: transparent;

    margin: 0;
    padding: 0;
    line-height: 0px;
    width: 100%;
    flex: 1 1 0;
    overflow-wrap: normal;
}

.input:focus {
    outline: none;
}

.heading-input {
    font-size: 28px;
    font-weight: 600;

}

.input::placeholder {

    opacity: 0.5;

}

.colorinput{
    position: absolute;
    inset: 0;
    opacity: 0;
    width: 100%;
    height: 100%;
}

.color-div{
    position:relative;
}

.description-input {
    font-size: 14px;
    font-weight: 600;
    width: 80%;
}

.toggle-div {
    display: flex;
    align-items: center;
    justify-content: end;
    gap: 20px;
}

.toggle-div h4 {
    font-size: 16px;
    font-weight: bold;
}

.top-question {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.top-question>p {
    padding: 0px;
    margin: 0px;
}

.heading-div {
    /* background: #2152ff; */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px;
    border-radius: 20px;
}



.section-details>.input {
    color: white;
}

.section-details>.input::placeholder {
    color: white;
}


.section-actions {
    display: none;
    flex-direction: row-reverse;
    gap: 12px;


}

.heading-div:hover {
    .section-actions {
        display: flex;
    }
}


.section-actions>svg {
    background-color: rgba(255, 255, 255, 0.3);
    border-radius: 15px;
    cursor: pointer;
}


.questions {
    padding: 0px 10px;
    display: flex;
    justify-content: start;
    align-items: stretch;
    gap: 20px;
    width: 100%;
    flex-direction: column;
}

.question {
    background-color: white;
    padding: 20px;
    border-radius: 20px;

    display: flex;
    flex-direction: column;
    gap: 30px;
    position: relative;
}

.type-question {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 9px 20px;
    height: 55px;
    border-radius: 14px;
    border: 1px solid #b6b6b6;
    color: #b6b6b6;
    background-color: #f8f9fa;
    cursor: pointer;
    user-select: none;

}

.type-question-div {
    position: relative;
    width: 50%;
}


.shadow {

    box-shadow: -12px 12px 12px 2px black;

}

.answer-type-2 {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    /* padding: 10px 20px; */
    /* height: 50px; */
    gap: 9px;
    width: 100%;
    /* border-radius: 12px; */
    cursor: pointer;
}

.answer-type-2 h5 {
    padding: 0px;
    margin: 0px;
    /* color: #999999; */
}

.plus {
    width: 40px;
    height: 40px;
}



.button-div {
    display: flex;
    padding: 10px 20px;
    gap: 20px;

}

.create-button {
    border: none;
    border-radius: 20px;
    color: white;
    /* background-attachment:  ; */

    display: flex;
    justify-content: center;
    align-items: center;
    gap: 5px;
    padding: 10px 17px;
    font-weight: 700;
    font-size: 18px;

    background: rgba(33, 82, 255,0.05) ;

    border: 3px solid #2152ff;
    color: #2152ff;
    transition: all 250ms ease-out;
}


.create-button:hover {

    color: white;
    /* -webkit-text-fill-color: white; */
    background: #2152ff;

    .plus path {
        fill: white;
    }
}

.question-icons {
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: absolute;
    top: 0px;
    right: -40px;
}


.question-icons svg {
    background-color: white;
    border-radius: 100%;
    cursor: pointer;
}
</style>