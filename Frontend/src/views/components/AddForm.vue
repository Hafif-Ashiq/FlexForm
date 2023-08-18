<template>
    <div class="modal-display ">
        <div class="add-display ">
            
                <h4 class="heading">
                Bring your new FlexForm to life
            </h4>
            <form @submit.prevent="addForm" class="form">
                <label for="name" class="label ">Give it a name</label>
                <soft-input id="form-name" type="text" placeholder="My form" name="name" v-model="form_name" />
                <soft-button class="my-4 mb-2" variant="gradient" color="info" full-width @click="() => addForm">
                    Continue
                </soft-button>
            </form>
            
            <div class="close"> 
                <img :src=cross alt="" class="close-img " @click="crossClicked">
            </div>
        </div>

    </div>
</template>
<script>
import SoftInput from "@/components/SoftInput.vue";
import SoftButton from "@/components/SoftButton.vue";
import cross from "../../assets/img/cross.svg"
import axios from "axios"
export default {
    components: {
        SoftInput,
        SoftButton
    },
    data() {
        return {
            form_name: "",
            cross
        }
    },
    methods: {
        async addForm() {
            if (this.form_name === "") {
                alert("Form must have a name: ")
                return
            }

            const data = {
                "title": this.form_name
            }

            axios.post("http://localhost:8000/form-api", data, {

                headers: {
                    Authorization: "token " + localStorage.getItem('token')
                }

            })
            .then(response => {

                if (response.status == 200) {
                        
                        // this.crossClicked()
                        this.$router.push({path : `/workspace/create-form/${response.data.data.id}` } )
                        
                    }
                })
                .catch(error => {
                    console.log(error);
                });

        },
        crossClicked() {
            this.$emit('close-modal')
        }
    }
}
</script>
<style scoped>
.modal-display{
    position: fixed;
    inset: 0;
    display: flex;
  justify-content: center;
  background-color: #000000da;
  z-index: 20;
}

.add-display{
    text-align: center;
  background-color: rgb(235, 235, 235);
  height: 400px;
  width: 500px;
  margin-top: 10%;
  padding: 60px 0;
  border-radius: 15px;
  position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 60px;
 
}

.close {
    position: absolute;

  /* margin: ; */
  top: 20px;
  right: 20px;
  cursor: pointer;
  background: white;
  border-radius: 100%;
}
.form{
    width: 70%;
}

.close-img {
  width: 30px;
}
.label{
    font-size: 16px;
    text-align: left;
    width: 100%;
}

</style>