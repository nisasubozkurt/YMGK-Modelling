
const chaos_maps = [
    {
        id:"bernoulli",
        name: "Bernoulli Map",
        description: "Kaostatik Bernoulli haritası, kaotik dinamik sistemler alanında önemli bir yere sahip olan basit bir ayrık zamanlı haritadır. Bu harita, basit doğrusal bir dönüşüm uygulayarak kaotik davranış sergiler. ",
        inputs: [
            "r",
            "iterations",
        ]
    },
    {
        id:"gingerbreadman",
        name: "Gingerbreadman Map",
        description: "Gingerbreadman metodu, karmaşıklık teorisi ve kaotik sistemlerin matematiksel analizinde önemli bir araç olarak kullanılır. Analizler, sistemlerin doğasını daha iyi anlamamıza ve belirli koşullar altında nasıl davrandıklarını öngörmemize yardımcı olabilir.",
        inputs: [
            "x_start",
            "y_start",
            "iterations",
        ]
    },
]

export default chaos_maps;