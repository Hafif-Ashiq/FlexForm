<template>
    <div class="py-4 container-fluid relative-position">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4" v-if="loaded">
                    <div class="card-header pb-0">
                        <h6>{{ form['title'] }}</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead>
                                    <tr>
                                        <th class="text-uppercase  text-secondary text-xxs font-weight-bolder opacity-7">
                                            #
                                        </th>
                                        <th class="text-uppercase  text-secondary text-xxs font-weight-bolder opacity-7">
                                            Approved
                                        </th>
                                        <th
                                            class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                                            Submit Time
                                        </th>


                                        <th class="text-secondary opacity-7"></th>
                                        <th class="text-secondary opacity-7"></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(response, index) in responses" :key="index">
                                        <td>
                                            <div class="px-3 font-weight-bold  ">
                                                {{ index + 1 }}
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex px-2 py-1 font-weight-bold ">
                                                {{ response['approved'] ? "Approved" : "Not-Approved" }}
                                            </div>
                                        </td>
                                        <td>
                                            <p class="text-sm font-weight-bold mb-0">{{ getDateTime(response['created_at'])
                                            }}</p>
                                            <!-- <p class="text-xs text-secondary mb-0">Organization</p> -->
                                        </td>


                                        <td class="align-middle text-center col-1">
                                            <SoftButton variant="gradient" class="mx-6 py-3" color="info" :active="true"
                                                size="sm" @click="viewResponse(response)">
                                                <!-- View SVG -->
                                                <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none"
                                                    xmlns="http://www.w3.org/2000/svg">
                                                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                                                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round"
                                                        stroke-linejoin="round"></g>
                                                    <g id="SVGRepo_iconCarrier">
                                                        <path
                                                            d="M9.75 12C9.75 10.7574 10.7574 9.75 12 9.75C13.2426 9.75 14.25 10.7574 14.25 12C14.25 13.2426 13.2426 14.25 12 14.25C10.7574 14.25 9.75 13.2426 9.75 12Z"
                                                            fill="#ffffff"></path>
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                            d="M2 12C2 13.6394 2.42496 14.1915 3.27489 15.2957C4.97196 17.5004 7.81811 20 12 20C16.1819 20 19.028 17.5004 20.7251 15.2957C21.575 14.1915 22 13.6394 22 12C22 10.3606 21.575 9.80853 20.7251 8.70433C19.028 6.49956 16.1819 4 12 4C7.81811 4 4.97196 6.49956 3.27489 8.70433C2.42496 9.80853 2 10.3606 2 12ZM12 8.25C9.92893 8.25 8.25 9.92893 8.25 12C8.25 14.0711 9.92893 15.75 12 15.75C14.0711 15.75 15.75 14.0711 15.75 12C15.75 9.92893 14.0711 8.25 12 8.25Z"
                                                            fill="#ffffff"></path>
                                                    </g>
                                                </svg>
                                            </SoftButton>

                                        </td>
                                        <td class="align-middle col-1">
                                            <SoftButton variant="gradient" class="mx-6 py-3" color="danger" :active="true"
                                                size="sm" @click="deleteResponse(response)">
                                                <!-- Delete SVG -->
                                                <!DOCTYPE svg
                                                    PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

                                                <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
                                                <svg width="22px" height="22px" viewBox="0 0 24 24" fill="none"
                                                    xmlns="http://www.w3.org/2000/svg">

                                                    <g id="SVGRepo_bgCarrier" stroke-width="0" />

                                                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round"
                                                        stroke-linejoin="round" />

                                                    <g id="SVGRepo_iconCarrier">
                                                        <path
                                                            d="M3 6.38597C3 5.90152 3.34538 5.50879 3.77143 5.50879L6.43567 5.50832C6.96502 5.49306 7.43202 5.11033 7.61214 4.54412C7.61688 4.52923 7.62232 4.51087 7.64185 4.44424L7.75665 4.05256C7.8269 3.81241 7.8881 3.60318 7.97375 3.41617C8.31209 2.67736 8.93808 2.16432 9.66147 2.03297C9.84457 1.99972 10.0385 1.99986 10.2611 2.00002H13.7391C13.9617 1.99986 14.1556 1.99972 14.3387 2.03297C15.0621 2.16432 15.6881 2.67736 16.0264 3.41617C16.1121 3.60318 16.1733 3.81241 16.2435 4.05256L16.3583 4.44424C16.3778 4.51087 16.3833 4.52923 16.388 4.54412C16.5682 5.11033 17.1278 5.49353 17.6571 5.50879H20.2286C20.6546 5.50879 21 5.90152 21 6.38597C21 6.87043 20.6546 7.26316 20.2286 7.26316H3.77143C3.34538 7.26316 3 6.87043 3 6.38597Z"
                                                            fill="#fff" />
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                            d="M11.5956 22.0001H12.4044C15.1871 22.0001 16.5785 22.0001 17.4831 21.1142C18.3878 20.2283 18.4803 18.7751 18.6654 15.8686L18.9321 11.6807C19.0326 10.1037 19.0828 9.31524 18.6289 8.81558C18.1751 8.31592 17.4087 8.31592 15.876 8.31592H8.12404C6.59127 8.31592 5.82488 8.31592 5.37105 8.81558C4.91722 9.31524 4.96744 10.1037 5.06788 11.6807L5.33459 15.8686C5.5197 18.7751 5.61225 20.2283 6.51689 21.1142C7.42153 22.0001 8.81289 22.0001 11.5956 22.0001ZM10.2463 12.1886C10.2051 11.7548 9.83753 11.4382 9.42537 11.4816C9.01321 11.525 8.71251 11.9119 8.75372 12.3457L9.25372 17.6089C9.29494 18.0427 9.66247 18.3593 10.0746 18.3159C10.4868 18.2725 10.7875 17.8856 10.7463 17.4518L10.2463 12.1886ZM14.5746 11.4816C14.9868 11.525 15.2875 11.9119 15.2463 12.3457L14.7463 17.6089C14.7051 18.0427 14.3375 18.3593 13.9254 18.3159C13.5132 18.2725 13.2125 17.8856 13.2537 17.4518L13.7537 12.1886C13.7949 11.7548 14.1625 11.4382 14.5746 11.4816Z"
                                                            fill="#fff" />
                                                    </g>

                                                </svg>
                                            </SoftButton>

                                        </td>
                                    </tr>

                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="link-copied bg-danger" v-if="deletedResponse">
            <p>Deleted Response!!!</p>
        </div>

    </div>
    <!-- <div v-if="responseShow">
        {{ responseShow }}
    </div> -->
    <response-modal v-if="responseShow" @update-responses="handleReload" :key="keyComp" :responseData="responseShow" :form_id="id"
        @close-response="closeModal"></response-modal>
</template>
  
<script>
import axios from 'axios'
import SoftButton from "@/components/SoftButton"
import ResponseModal from './components/ResponseModal.vue';
export default {
    props: ['id'],
    components: {
        SoftButton,
        ResponseModal
    },
    data() {
        return {
            url: "http://localhost:8000/",
            loaded: false,
            keyComp:0,
            responses: [],
            form: '',
            responseShow: false,
            deletedResponse:false
        };
    },
    async mounted() {

        const formData = await axios.get(this.url + "get-form/" + this.id, {

            headers: {
                Authorization: "token " + localStorage.getItem('token')
            }

        })
        this.form = formData.data.data


        this.handleReload()


    },
    methods: {
        closeModal() {
            this.responseShow = false
            this.keyComp++
        },
        async deleteResponse(response) {
            if (confirm("Are you sure to delete this response?")) {
                const data = {
                    'form_id': this.id,
                    'response_id': response['id']
                }
                console.log(data);
                await axios.delete(this.url + 'delete-response', {
                    headers: {
                        Authorization: "token " + localStorage.getItem('token')
                    },
                    data: data
                })
                    .then(response => {
                        console.log(response);
                        this.deletedResponse = true
                        setTimeout(() => {
                            this.deletedResponse = false
                        }, 2000)
                        this.handleReload()
                    })
            }
        },
        async handleReload() {
            const resdata = await axios.get(this.url + "get-response/" + this.id, {

                headers: {
                    Authorization: "token " + localStorage.getItem('token')
                }


            })



            const responseData = await resdata.data


            this.responses = responseData
            this.responses.sort((a, b) => {
                return a.id - b.id;
            });
            this.loaded = true
        },
        viewResponse(response) {

            this.responseShow = response
            console.log(response);
        },
        getDateTime(dateTime) {
            const createdDate = new Date(dateTime)
            var date = createdDate.toLocaleDateString();

            var time = createdDate.toLocaleTimeString().replace(/(.*)\D\d+/, '$1');
            return date + "  " + time
        }
    }


};
</script>
  

<style>
.relative-position {
    position: relative;
}

.link-copied {
    position: fixed;
    right: 20px;
    bottom: 20px;
    width: 350px;
    height: 70px;
    /* background-color: green; */
    display: grid;
    place-items: center;
    border-radius: 18px;
    box-shadow: -2px -2px 12px 2px rgb(63, 63, 63);


}

.link-copied p {
    font-size: 20px;
    color: white;
    font-weight: 600;

    margin: 0px;
    padding: 0px;
}
</style>