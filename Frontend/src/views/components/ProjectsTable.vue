<template>
  <div class="card mb-4 ">
    <div class="card-header pb-0 table-head">
      <h5>Forms </h5>
      <SoftButton variant="gradient" class="mx-6 py-3" color="info" :active="true" size="md" @click="show_add = true">Add
        Form</SoftButton>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center justify-content-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Form Name
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                Questions
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                Responses
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                Status
              </th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(form, index) in forms" class="form-entry" :key="form['id']"
              @click="form['published'] ? getResponses(form['id']) : createForm(form['id'])">
              <td>
                <div class="d-flex px-4">
                  <div class="my-auto">
                    <h6 class="mb-0 text-sm">{{ form['title'] }}</h6>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-sm font-weight-bold mb-0 px-4">{{ form['total_questions'] }}</p>
              </td>
              <td>
                <span class="text-xs font-weight-bold px-4">{{ form['responses'] ? form['responses'] : "---" }}</span>
              </td>
              <td>
                <span class="mb-0 text-sm font-weight-bold">{{ form['published'] ? "Published" : "Unpublished" }}</span>
              </td>
              <td class="align-center " @click="menuOpen === index ? menuOpen = -1 : menuOpen = index">
                <div class="options">

                  <SoftButton variant="gradient" class="" color="info" :active="true" size="md" v-if="form['published']"
                    @click.stop="copyLink(form['id'])">
                    <!-- Copy SVG -->
                    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

                    <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
                    <svg width="25px" height="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">

                      <g id="SVGRepo_bgCarrier" stroke-width="0" />

                      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" />

                      <g id="SVGRepo_iconCarrier">
                        <path
                          d="M16 12.9V17.1C16 20.6 14.6 22 11.1 22H6.9C3.4 22 2 20.6 2 17.1V12.9C2 9.4 3.4 8 6.9 8H11.1C14.6 8 16 9.4 16 12.9Z"
                          fill="#ffffff" />
                        <path opacity="0.4"
                          d="M17.0998 2H12.8998C9.44976 2 8.04977 3.37 8.00977 6.75H11.0998C15.2998 6.75 17.2498 8.7 17.2498 12.9V15.99C20.6298 15.95 21.9998 14.55 21.9998 11.1V6.9C21.9998 3.4 20.5998 2 17.0998 2Z"
                          fill="#ffffff" />
                      </g>

                    </svg>
                  </SoftButton>


                </div>
              </td>
              <td class="align-center " @click="menuOpen === index ? menuOpen = -1 : menuOpen = index">
                <div class="options">

                  <SoftButton variant="gradient" class="" color="danger" :active="true" size="md"
                    @click.stop="deleteForm(form['id'])">
                    <!-- Bin SVG -->
                    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
                    <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">

                      <g id="SVGRepo_bgCarrier" stroke-width="0" />

                      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" />

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


                </div>
              </td>

            </tr>
            <add-form v-if="show_add" @close-modal="closeModal" />
          </tbody>
        </table>
      </div>
    </div>
    <div class="link-copied bg-info" v-if="linkCopied">
      <p>Response Link copied!!!</p>
    </div>
    
  </div>
</template>

<script>
// import SoftProgress from "@/components/SoftProgress";
import SoftButton from "@/components/SoftButton"
import AddForm from "./AddForm.vue";

export default {
  name: "projects-table",
  components: {
    // SoftProgress,
    SoftButton,
    AddForm
  },
  props: ["forms", "responses"],
  data() {
    return {
      show_add: false,
      menuOpen: -1,
      client_url: "http://localhost:8080/",
      linkCopied : false,
      deletedForm : false
    }
  },
  methods: {
    closeModal() {
      this.show_add = false
      this.$emit('reload')
    },
    deleteForm(id) {
      this.$emit('delete-form', id)
    },
    createForm(id) {

      this.$router.push({ path: `/workspace/create-form/${id}` })
    },
    getResponses(id) {
      console.log(id);
      console.log(this.responses[id]);
      this.$router.push({ path: `/workspace/form-responses/${id}` })

    },
    copyLink(id) {
      navigator.clipboard.writeText(this.client_url + "form/" + id)
      this.linkCopied = true
      setTimeout(()=>{
        this.linkCopied = false
      },2000)
    }
  }
}

</script>


<style scoped>

.link-copied{
  position: fixed;
  right: 20px;
  bottom: 20px;
  width: 350px;
  height: 70px;
  /* background-color: green; */
  display: grid;
  place-items: center;
  border-radius: 18px;
  box-shadow: -2px -2px 12px 2px rgba(147, 147, 147, 0.432);
  
  
}
.link-copied p{
  font-size: 20px;
  color: white;
  font-weight: 600;

  margin: 0px;
  padding: 0px;
}
.options {
  position: relative;
  text-align: center;
}

.optionsOverlay {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  flex-direction: column;
  position: absolute;
  top: 15px;
  left: 40px;
  /* transform:  ; */
  background-color: #f9f9f9;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 10;
  border-radius: 10px;

}

.optionButton {
  width: 100%;
  padding: 5px 20px;
  text-align: left;
  border: none;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 14px;

}

.delete-button {
  border-radius: 10px;
}


.delete-button:hover {
  background-color: #dc3545;
  color: white;
}

.form-entry {
  cursor: pointer;

}

.form-entry:hover {
  background: rgb(235, 235, 235);
}


.table-head {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

}
</style>