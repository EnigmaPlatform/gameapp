class MainActivity : AppCompatActivity() {
    private lateinit var player: Player
    private lateinit var adapter: StatsAdapter
    private lateinit var sharedPreferences: SharedPreferences
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        sharedPreferences = getPreferences(Context.MODE_PRIVATE)
        val isFirstRun = sharedPreferences.getBoolean("is_first_run", true)
        
        if (isFirstRun) {
            showWelcomeDialog()
        } else {
            initializeApp()
        }
    }
    
    private fun showWelcomeDialog() {
        val dialog = AlertDialog.Builder(this, R.style.NeonDialogTheme)
            .setTitle("ТЫ ИГРОК?")
            .setCancelable(false)
            .setPositiveButton("Да") { _, _ ->
                sharedPreferences.edit().putBoolean("is_first_run", false).apply()
                initializeApp()
            }
            .setNegativeButton("Нет") { _, _ ->
                Toast.makeText(this, "Игрок не найден", Toast.LENGTH_LONG).show()
                Handler(Looper.getMainLooper()).postDelayed({
                    finish()
                }, 2000)
            }
            .create()
            
        dialog.show()
        
        dialog.window?.let {
            it.setBackgroundDrawableResource(R.drawable.neon_border)
            it.attributes?.dimAmount = 0.8f
        }
        
        val titleView = dialog.findViewById<TextView>(android.R.id.title)
        titleView?.setTextColor(ContextCompat.getColor(this, R.color.neon_blue))
        titleView?.textSize = 24f
        titleView?.typeface = Typeface.DEFAULT_BOLD
    }
    
    private fun initializeApp() {
        setContentView(R.layout.activity_main)
        
        player = Player()
        setupUI()
        setupButtons()
    }
    
    private fun setupUI() {
        val recyclerView = findViewById<RecyclerView>(R.id.statsRecyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        
        adapter = StatsAdapter(player.stats) { statName ->
            player.upgradeStat(statName)
            updateUI()
        }
        recyclerView.adapter = adapter
        
        updateUI()
    }
    
    private fun setupButtons() {
        val addExpButton = findViewById<Button>(R.id.addExpButton)
        addExpButton.setOnClickListener {
            player.addExperience(20)
            updateUI()
        }
    }
    
    private fun updateUI() {
        findViewById<TextView>(R.id.levelText).text = "Уровень: ${player.level}"
        findViewById<TextView>(R.id.talentText).text = "Очки талантов: ${player.talentPoints}"
        
        val expProgress = findViewById<ProgressBar>(R.id.expProgressBar)
        expProgress.max = player.experienceToNextLevel
        expProgress.progress = player.experience
        
        findViewById<TextView>(R.id.expText).text = 
            "Опыт: ${player.experience}/${player.experienceToNextLevel}"
        
        adapter.notifyDataSetChanged()
    }
}
