window.onload = new Vue({
    el: '#app',
    data: {
        playerLife: 100,
        monsterLife: 100,
        result: "Result",
        startGame: true,
        gameOver: false,
        gameLog: false,
        playerLog: [],
        monsterLog: [],
        player_damage: 0,
        monster_damage: 0,
        give_up: false
    },
    computed: {

    },
    methods: {
        playerAttack: function(dmg_modfied=10, attack_type="normal"){
            this.player_damage = Math.round(parseInt(dmg_modfied) * (1 + Math.random()))
            this.monsterLife -= this.player_damage
            this.playerLog.push("The player use " +attack_type+ " hit and the monster lost: " + this.player_damage + " of life")
        },
        monsterAttack: function(){
            this.monster_damage = Math.round(10 * (1 + Math.random()))
            this.playerLife -= this.monster_damage
            this.monsterLog.push("The monster hit the player with " + this.monster_damage + " dmg")
        },
        attack: function() {
            this.playerAttack()
            this.monsterAttack()
            this.gameLog = true
        },
        super_attack: function() {
            this.playerAttack(dmg_modfied=20, attack_type="SUPER")
            this.monsterAttack()
        },
        heal: function() {
            this.player_heal = Math.round(10 * (1 + Math.random()))
            this.playerLife += this.player_heal
            this.playerLog.push("The player healed himself with: " + this.player_heal)
            this.monsterAttack()
        },
        start_game() {
            this.playerLife = 100
            this.monsterLife = 100
            this.startGame = true
            this.gameOver = false
            this.gameLog = false
            this.playerLog = []
            this.monsterLog = []
            this.player_damage = 0
            this.monster_damage = 0
            this.give_up = false
        }

    },
    watch: {
        monsterLife() {
            if (this.monsterLife <= 0) {
                this.gameOver = true
                this.result = "The players defeat the monster"
                this.monsterLife = 0
            }
        },
        playerLife() {
            if (this.playerLife <= 0) {
                this.gameOver = true
                this.result = "The players was defeated by monster"
                this.playerLife = 0
            }
        },
        give_up() {
            if (this.give_up){
                this.gameOver = true
                this.result = "The players give up"      
                this.playerLog.push("This idiot give up")          
            }
        }    
    }
})