
const chaos_maps = [
    {
        id:"generate_and_save_bernoulli_map",
        name: "Bernoulli Map",
        description: "Kaostatik Bernoulli haritası, kaotik dinamik sistemler alanında önemli bir yere sahip olan basit bir ayrık zamanlı haritadır. Bu harita, basit doğrusal bir dönüşüm uygulayarak kaotik davranış sergiler. ",
        inputs: [
            "r",
            "x0",
            "num_iterations",
        ]
    },
    {
        id:"generate_gingerbread_map",
        name: "Gingerbreadman Map",
        description: "Gingerbreadman metodu, karmaşıklık teorisi ve kaotik sistemlerin matematiksel analizinde önemli bir araç olarak kullanılır. Analizler, sistemlerin doğasını daha iyi anlamamıza ve belirli koşullar altında nasıl davrandıklarını öngörmemize yardımcı olabilir.",
        inputs: [
            "x_start",
            "y_start",
            "iterations",
        ]
    },
    {
        id:"generate_and_save_tent_map",
        name:"Tent Map",
        description:"Çadır haritası, dinamik sistemleri temsil etmek için kullanılan matematiksel bir kavramdır. Özellikle kaos teorisini incelemek için oldukça kullanışlıdır. Çadır haritası, bir boyutta uygulanan parça doğrusal bir fonksiyondur. Kullanılan μ parametresine bağlı olarak karmaşık davranışlar gösterebilir. Görsel olarak fonksiyonun grafiği bir çadır şeklini andırır, bu nedenle bu isimle anılır.",
        inputs: [
            "x",
            "r",
            "iterations"
        ]
    },
    {
        id:"generate_tinkerbell_map",
        name:"Tinkerbell Map",
        description:"Tinkerbell haritası, basit bir matematiksel modeldir. Kaos teorisinin temel ilkelerini göstermek için kullanılabilir. Görsel olarak çekici ve ilgi çekici bir modeldir ve karmaşık ve kaotik davranışları göstermek için kullanılabilir.",
        inputs: [
            "a",
            "b",
            "c",
            "d",
            "iterations"
        ]
    },
    {
        id:"generate_and_save_lorenz96_map",
        name:"Lorenz96 Map",
        description:"",
        inputs: [
            "N ",
            "F",
            "dt",
            "num_steps"
        ]
    },
    {
        id:"generate_and_save_logistic_map",
        name:"Logistic Map",
        description:"Logistic haritası, bir populasyonun zaman içindeki değişimini modellemek için kullanılan bir matematiksel modeldir. İlk olarak 1976'da Robert May tarafından tanıtılmıştır. Bu model, belirli bir populasyonun gelecekteki durumunu tahmin etmek için kullanılırken, kaotik davranışları da gösterebilir.",
        inputs: [
            "r",
            "x0",
            "iterations"
        ]
    },
    {
        id: "generate_and_save_henon_map",
        name: "Henon Map",
        description: "Henon haritası, dinamik sistemlerin ve kaotik davranışın matematiksel modellenmesinde kullanılan bir sistemdir. Çift haneleli bir denkleme dayanır ve karelerin geri dönüşümü ile tanımlanır.",
        inputs: [
            "a",
            "b"
        ]
    }
]

export default chaos_maps;