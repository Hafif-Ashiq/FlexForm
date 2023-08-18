<template >
    <div class="screen" v-if="laoded">

        <div class="top-section">
            <div class="header-section ">

                <div class="header">
                    <input type="text" spellcheck='false' class="heading-input input" v-model="title"
                        placeholder="Form Name">
                    <input type="text" spellcheck='false' class="description-input input" v-model="description"
                        placeholder="Description(click to edit)">

                </div>

                <div class="publish-div">
                    <soft-button class="my-4 mb-2 button" size="md" color="info" @click="handleSave">
                        Save
                    </soft-button>
                    <soft-button class="my-4 mb-2 button" size="md" color="info" @click="handlePublish">
                        Publish Form
                    </soft-button>
                </div>
            </div>
            <div class="line"></div>
        </div>

        <div class="form-creator">
            <div class="form-editor" :key="componentKey">

                <!-- <Sortable :list="sections" item-key="index" tag="div" :options="options">
                    <template #item="{ section, index }"> -->

                <SectionForm v-for="(section, index) in sections" :key="index" :section="section" :indexSect="index"
                    :total-sects="sections.length" :loaded="laoded"
                    @data-changed="(data) => handleSectionChange(index, data)" @add-section="sectionAdd"
                    @copy-section="sectionCopy(index)" @delete-section="deleteSection(index)" />
                <!-- </template>
                </Sortable> -->

            </div>
            <div class="form-preview">
                <form-viewer :title="title" :description="description" :sections="sections" />
            </div>
        </div>
    </div>
</template>
<script>
import SoftButton from "@/components/SoftButton.vue";
// import draggable from "vuedraggable";
// import FormViewer from "../components/FormViewer.vue"
// import ViewForm from "../components/ViewForm.vue"
// import { Sortable } from "sortablejs-vue3"
import FormViewer from "./FormViewer.vue";
import SectionForm from "./components/SectionForm.vue";

import axios from 'axios'


export default {
    components: {
        SoftButton,
        SectionForm,
        FormViewer,
        // Sortable
        // draggable
    },
    props: ['id'],
    async mounted() {


        const data = await axios.get('http://localhost:8000/get-form/' + this.id, {

            headers: {
                Authorization: "token " + localStorage.getItem('token')
            }

        })

        const apiData = data['data']
        console.log(apiData);
        this.title = apiData['data']['title']
        this.description = apiData['data']['description']
        
        if (apiData['data']['meta'] !== '') {

            const meta = JSON.parse(apiData['data']['meta'])

            this.sections = meta['sections']


        }
        if (!apiData['data']['published']) {
            this.laoded = true
        }
        


    },
    data() {
        return {
            options: {
                handle: '.glyphicon-move',
                animation: 150
            },
            list: [
                { name: "Navigation", text: "", id: 0 },
                { name: "Contact", text: "", id: 1 },
                { name: "Products", text: "", id: 2 },
            ],
            laoded: false,
            componentKey: 0,
            title: '',
            description: '',

            sections: [{
                'title': "",
                'color': "#2152ff",
                'questions': [
                    {
                        isRequired: false,
                        question: "",
                        description: "",
                        type: '',
                        data: {
                            'placeholder': null,
                            'options': null
                        },
                    }
                ]
            }]
        }
    },
    watch: {

    },
    methods: {

        handleSave() {

            const saveData = {
                'id': this.id,
                'title': this.title,
                'description': this.description,
                'meta': JSON.stringify({
                    'sections': this.sections
                })
            }

            console.log({
                'id': this.id,
                'title': this.title,
                'description': this.description,
                'meta': {
                    'sections': this.sections
                }
            });


            axios.patch('http://localhost:8000/form-api', saveData, {

                headers: {
                    Authorization: "token " + localStorage.getItem('token')
                }

            })
                .then(response => {

                    console.log(response);

                })
                .catch(error => {
                    console.log(error);
                })

            this.$router.push({ path: `/workspace/` })

        },
        handlePublish() {
            
            const publishData = {
                'id': this.id,
                'title': this.title,
                'description': this.description,
                'meta': JSON.stringify({
                    'sections': this.sections
                }),
                
            }
            
            axios.patch('http://localhost:8000/publish-form', publishData, {

                headers: {
                    Authorization: "token " + localStorage.getItem('token')
                }

            })
                .then(response => {

                    console.log(response);
                    if (response.status == 200) {
                        this.$router.push({ path: `/workspace/` })
                    }
                })
                .catch(error => {
                    console.log(error);
                    alert("Couldn't publish form")
                    this.$router.push({ path: `/workspace/` })
                })

            

        },
        sectionAdd() {
            this.sections.push({
                'title': "",
                'color': '',
                'questions': [
                    {
                        isRequired: false,
                        question: "",
                        description: "",
                        type: '',
                        data: {
                            'placeholder': null,
                            'options': null
                        },
                    }
                ]
            })

            this.handleReload()
        },
        handleSectionChange(index, data) {

            this.sections[index] = data
            this.$forceUpdate()

        },
        sectionCopy(index) {

            this.sections.push({
                'title': this.sections[index]['title'],
                'color': this.sections[index]['color'],
                'questions': this.sections[index]['questions']
            })
            this.handleReload()
        },
        deleteSection(index) {


            this.sections.splice(index, 1)


            this.handleReload()
        },
        handleReload() {
            this.componentKey += 1
        }
    },
}
</script>
<style scoped>
:root {
    --main: #141727
}

.ghost {
    opacity: 0.5;
    background: #c8ebfb;
}

.screen {
    padding-left: 50px;
    padding-right: 50px;

    display: flex;
    flex-direction: column;
    gap: 50px;
    user-select: none;
}

.top-section {
    display: flex;
    flex-direction: column;
    gap: 30px;

}

.line {
    width: 100%;
    height: 2px;
    background: #c6c6c6;
}

.header-section {


    display: flex;
    justify-content: space-between;
    align-items: center;
}

.row-col {
    background: #000;
    height: 100%;
}

.row-col div {
    height: 100%;
    background-color: aqua;
    border: 1px solid black;
}

.header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    gap: 0px;
    flex: 1;
}

.input {
    border: none;
    background: inherit;
    color: #141727;


}

.publish-div {
    display: flex;
    align-items: center;
    justify-content: end;
    gap: 50px;
}

.input:focus {
    outline: none;
}

.heading-input {
    font-size: 32px;
    font-weight: 700;
    width: 80%;
}

.description-input {
    font-size: 18px;
    font-weight: 500;
    width: 80%;
}

.button {
    border-radius: 15px;
    background-color: #2152ff;
    padding: 25px 45px;

    font-size: 16px;
    letter-spacing: 1px;


}

.button:hover {
    background-color: #2152ff;

}

.form-creator {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 150px;
}

.form-editor {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: stretch;
    gap: 40px;
    padding-top: 20px;
}
</style>