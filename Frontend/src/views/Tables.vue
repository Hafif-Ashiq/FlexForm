<template>
  <div class="py-4 container-fluid">

    <div class="row">
      <div class="col-12" v-if="loaded">
        <projects-table :forms="forms" :responses="responses" @reload="handleReload" @delete-form="deleteForm" />
      </div>
      
    </div>
    <div class="link-copied bg-danger" v-if="deletedForm">
        <p>Deleted Form!!!</p>
    </div>
  </div>
</template>

<script>
// import AuthorsTable from "./components/AuthorsTable";
import ProjectsTable from "./components/ProjectsTable";
import axios from 'axios'
export default {
  name: "forms",
  components: {

    ProjectsTable,
  },
  mounted() {
    this.handleReload()
  },
  watch: {

  },
  data() {
    return {
      url: "http://localhost:8000/",
      forms: [],
      responses: {},
      loaded: false,
      deletedForm: false
    }
  }, methods: {
    async handleReload() {
      const data = await axios.get(this.url + "form-api", {

        headers: {
          Authorization: "token " + localStorage.getItem('token')
        }

      })
      this.forms = data.data

      console.log(this.forms);
      this.forms.forEach(async form => {

        let quests = 0
        const secs = JSON.parse(form['meta'])['sections']
        for (let i = 0; i < secs.length; i++) {
          for (let j = 0; j < secs[i]['questions'].length; j++) {
            // secs[i]['questions'][j]['index'] = index

            quests++
          }

        }
        form['total_questions'] = quests


        if (form['published']) {
          Promise.all([this.getResponses(form)]).then(responseData => {
            // console.log(responseData);
            form['responses'] = 0 + responseData[0].length
            // console.log(form['responses']);
            this.responses[form['id']] =  responseData[0]
          })

        }



      });

      this.forms.sort((a, b) => {
            return a.id - b.id;
        });
      this.loaded = true
    },
    async getResponses(form) {

      const resdata = await axios.get(this.url + "get-response/" + form['id'], {

        headers: {
          Authorization: "token " + localStorage.getItem('token')
        }

      })



      const responseData = resdata.data
      // console.log(responseData);
      // form['responses'] = 0
      // form['responses'] = responseData.length
      return responseData

      // this.responses[form['id']] = responseData
    },
    async deleteForm(value) {
      if (confirm("Are you sure to delete this form?")) {
        console.log(localStorage.getItem('token'));
        console.log(value);
        const data = {
          'id': value
        }
        axios.delete(this.url + "form-api", {
          headers: {
            Authorization: "token " + localStorage.getItem('token')
          },
          data: data
        }
        ).then(response => {
          if ((response.status == 200)) {

            this.deletedForm = true
            setTimeout(() => {
              this.deletedForm = false
            }, 2000)

          }
          this.handleReload()
        })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
}
</script>
<style>
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
  box-shadow: -2px -2px 12px 2px rgb(138, 138, 138);


}
.link-copied p{
  font-size: 20px;
  color: white;
  font-weight: 600;

  margin: 0px;
  padding: 0px;
}
</style>