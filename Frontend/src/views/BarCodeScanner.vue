<template>
    <div class="main-div">
        <h3 class="form-heading">Bar Code Scanner</h3>
        <div class="camera" v-if="!resultFound">
            <StreamBarcodeReader  @decode="onDecode" @loaded="onLoaded" @result="displayResult"></StreamBarcodeReader>
        </div>
        <div class="result" v-if="resultFound">
            <div class="result-data">
                <h3>Result: </h3>
            <p>{{ resultData }}</p>
            </div>
            <!-- <button>Go back</button> -->
            <SoftButton variant="gradient" class="mx-6 py-3" color="info" :active="true" size="sm" @click="goBack"> Go Back</SoftButton>
        </div>
        <!-- <ImageBarcodeReader @decode="onDecode" @error="onError"></ImageBarcodeReader> -->
    </div>
</template>
<script>

const body = document.getElementsByTagName("body")[0];
import { StreamBarcodeReader } from "@teckel/vue-barcode-reader";
import SoftButton from "@/components/SoftButton"

export default {
    components: {
        StreamBarcodeReader,
        SoftButton,
    },
    data() {
        return {
            resultFound: false,
            resultData: null,
            key:0
        }
    },
    methods: {
        onDecode(result) {
            this.resultData = result
            this.resultFound = true
            console.log(result)
        },
        onLoaded() {
            console.log("loaded");
        },
        onError(e) {
            console.log(e);
        },
        displayResult(r) {
            console.log(r);
        },
        goBack(){
            this.resultData = null
            this.resultFound = false
            this.key+= 1
        }
    },


    beforeMount() {
        this.$store.state.showNavbar = false;
        this.$store.state.showSidenav = false;
        this.$store.state.showFooter = false;
        body.classList.add("virtual-reality");
        this.$store.state.isTransparent = "bg-white";
    },
    beforeUnmount() {
        this.$store.state.showNavbar = true;
        this.$store.state.showSidenav = true;
        this.$store.state.showFooter = true;
        body.classList.remove("virtual-reality");

        if (this.$store.state.isPinned === false) {
            const sidenav_show = document.querySelector(".g-sidenav-show");
            sidenav_show.classList.remove("g-sidenav-hidden");
            sidenav_show.classList.add("g-sidenav-pinned");
            this.$store.state.isPinned = true;
        }
        this.$store.state.isTransparent = "bg-transparent";
    },

}
</script>
<style scoped>
.camera {
    border-radius: 20px;
    overflow: hidden;
    /* width: 70%; */
    /* height: 70%; */
    /* background-color: rgb(112, 68, 11); */
}
.form-heading {
    font-size: 48px;
    font-weight: 800;
    color: #141727;
}
.main-div{
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: start;
    align-items: center;
    flex-direction: column;
    gap: 50px;
    padding: 70px;
}

.result{
    background-color: rgb(224, 224, 224);
    width: 60%;
    height: 60%;
    display: flex;
    justify-content: space-between;
    align-items: center;
 
    padding: 60px 50px;
    flex-direction: column;
    border-radius: 20px;
    box-shadow: -2px 2px 12px 2px rgba(35, 35, 35, 0.428);
}

.result-data{
    border-bottom: 2px solid white;
    display: flex;
    justify-content: space-between;
    width: 100%;
    align-items: center;
    > p{
        margin: 0;
        padding: 0;
        font-size: 22px;
    }
}

</style>