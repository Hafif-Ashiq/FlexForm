<template >
    <div class="screen-form">
        <div class="top-div">
            <h1 class="main-heading">Form Preview</h1>
            <div class="heading-div">
                <h3 class="form-heading">{{ title ? title : "Title Name" }}</h3>
                <p class="form-desc">{{ description ? description : "description" }}</p>
            </div>
        </div>
        <div class="sections-div">
            <div class="section" v-for="(section, index) in sections" :key="index">

                <div class="section-header">
                    <span class="section-num">{{ index + 1 }} of {{ sections.length }}</span>
                    <span class="section-heading">{{ section['title'] !== '' ? section['title'] : "Section Title" }}</span>
                    <div class="sect-color"
                        :style="section['color'] === '' ? { 'backgroundColor': '#2152ff' } : { 'backgroundColor': section['color'] }">
                    </div>
                </div>

                <div class="questions-div">
                    <div v-for="(question, index) in section['questions']" class="quest" :key="index">
                        <div class="question-head">
                            <span class="question-header">Question {{ index + 1 }}</span>
                            <span class="question-text">
                                <span class="question-body-text">
                                    {{ question['question'] === '' ? "Your Question" :
                                        question['question'] }}
                                </span>
                                <span v-if="question['isRequired']" class="required">*</span>
                            </span>
                            <span class="question-desc">{{ question['description'] === '' ? "Description" :
                                question['description'] }}</span>
                        </div>
                        <div class="inputField">
                            <!-- For Placeholders -->
                            <input v-if="placeholderNeeded(question['type'])" disabled class="input" type="text"
                                :placeholder="question['data']['placeholder'] === '' || !question['data']['placeholder'] ? 'Answer Placeholder' : question['data']['placeholder']">
                            <!-- For nothing -->
                            <input v-if="nothingNeeded(question['type'])" disabled class="input" :type="question['type']"
                                :placeholder="question['type']">
                            <!-- For Checkboxes -->
                            <div v-if="checkBoxNeeded(question['type'])">

                                <div v-for="(option, index) in question['data']['options']" class="check-div" :key="index">
                                    <label class="checkBox">

                                        <input id="ch1" disabled type="checkbox">
                                        <div class="transition"></div>
                                    </label>
                                    <label for="ch1" class="input-label">{{ option }}</label>
                                </div>
                            </div>
                            <div v-if="dropdown(question['type'])">

                                <div class="type-question">
                                    <p class="answer-type-1">{{ question['data']['options'][0] }}</p>
                                    <img src="../assets/icons/arrow-down.svg" alt="">
                                </div>
                            </div>
                            <div v-if="question['type'] === 'textarea'">
                                <textarea disabled name="" id="" cols="30" rows="20" class="textarea-input"></textarea>
                            </div>
                            <div v-if="question['type'] === 'radio'" class="radio-input">
                                <div v-for="(option, index) in question['data']['options']"
                                    :class="index === 0 ? 'radio-select' : ''" class="radio-opt" :key="index">
                                    {{ option }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: ['title', 'description', 'sections'],

    methods: {
        placeholderNeeded(type) {
            if (type === 'email' || type === 'password' || type === 'number' || type === 'text') {
                return true
            }
            return false
        },
        checkBoxNeeded(type) {
            if (type === 'multiplechoice' || type === 'checkbox') {
                return true
            }
            return false
        },
        nothingNeeded(type) {
            return type === 'date' || type === 'file' ? true : false
        },
        dropdown(type) {
            return type === 'dropdown'
        }
    }
}
</script>
<style scoped>
.screen-form {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
    gap: 40px;
    user-select: none;
}

.top-div {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: stretch;
    gap: 20px;
}

.main-heading {
    font-size: 36px;
    font-weight: 700;
    color: #141727;
}

p {
    position: relative;
    inset: 0;
    margin: 0;
}

.heading-div {
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: center;
    gap: 2px;
}

.form-heading {
    font-size: 28px;
    font-weight: 700;
    color: #141727;
}

.form-desc {
    font-size: 18px;
    font-weight: 600;
    color: #141727;
}

.section {
    color: #141727;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
    gap: 20px;
    padding: 10px 25px;
}

.section-header {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: stretch;
    gap: 1px;
    position: relative;
}

.section-heading {
    font-weight: 700;
    font-size: 24px;
    color: #141727;

}

.section-num {
    font-weight: 600;
    color: #141727;

}

.sect-color {
    width: 18px;
    border-radius: 20px;
    height: 100%;
    /* background: #000; */
    position: absolute;
    left: -30px;
    top: 0;

}


.question-header {
    color: #141727;
    font-size: 18px;
    font-weight: 700;

}

.question-text {
    color: #141727;
    font-size: 20px;
    font-weight: 800;
    display: flex;
    justify-content: start;
    align-items: start;
    gap: 5px;
    width: 90%;
}

.question-desc {
    color: #707070;
    font-weight: 600;
}

.question-head {
    display: flex;
    flex-direction: column;


}

.sections-div {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
    gap: 35px;
}

.questions-div {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: space-around;
    gap: 25px;
    padding: 10px;
}

.required {
    color: red;
    font-size: 20px;
}


.input {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 85%;
    padding: 16px 20px;
    height: 65px;
    border-radius: 14px;
    border: 1px solid #b6b6b6;
    /* border: none; */
    font-weight: 600;
    font-size: 17px;
    /* color: #dfdfdf; */
    background-color: #ededed;
    /* cursor: pointer; */
    user-select: none;
    /* box-shadow: -1px 1px 3px 0px gray; */

}

.textarea-input {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 30px 10px;
    height: 125px;
    border-radius: 14px;
    border: 1px solid #b6b6b6;
    resize: none;
    font-size: 16px;
    background-color: #ededed;
    user-select: none;


}

.input:focus {
    outline: none;
}

.quest {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
    gap: 20px;
}



.checkBox {
    display: block;
    cursor: pointer;
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255, 255, 255, 0);
    border-radius: 4px;
    position: relative;
    overflow: hidden;
    box-shadow: 0px 0px 0px 2px #2152ff;
}

.checkBox div {
    width: 60px;
    height: 60px;
    background-color: #2152ff;
    top: -52px;
    left: -52px;
    position: absolute;
    transform: rotateZ(45deg);
    z-index: 100;
}

.checkBox input[type=checkbox]:checked+div {
    left: -10px;
    top: -10px;
}

.checkBox input[type=checkbox] {
    position: absolute;
    left: 50px;
    visibility: hidden;
}

.transition {
    transition: 300ms ease;
}

.check-div {
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 4px;
}

.input-label {
    font-size: 18px;
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
    background-color: #ededed;



}

.radio-input {
    display: flex;
    background: #ededed;
    padding: 10px;
    justify-content: start;
    align-items: center;
    /* width: ; */
    width: max-content;
    border-radius: 20px;

}

.radio-opt {

    font-weight: 600;
    display: flex;
    padding: 30px;
    justify-content: center;
    align-items: center;
    /* width: 100%; */
    height: 100%;
    border-radius: 18px;
}

.radio-select {
    background: white;
}
</style>