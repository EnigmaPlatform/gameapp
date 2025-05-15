class StatsAdapter(
    private val stats: List<Stat>,
    private val onUpgradeClick: (String) -> Unit
) : RecyclerView.Adapter<StatsAdapter.StatViewHolder>() {

    class StatViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val name: TextView = view.findViewById(R.id.statName)
        val value: TextView = view.findViewById(R.id.statValue)
        val progress: ProgressBar = view.findViewById(R.id.statProgress)
        val upgradeButton: Button = view.findViewById(R.id.upgradeButton)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StatViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.stat_item, parent, false)
        return StatViewHolder(view)
    }

    override fun onBindViewHolder(holder: StatViewHolder, position: Int) {
        val stat = stats[position]
        holder.name.text = stat.name
        holder.value.text = stat.value.toString()
        holder.progress.progress = stat.progress
        
        holder.upgradeButton.setOnClickListener {
            onUpgradeClick(stat.name)
        }
    }

    override fun getItemCount() = stats.size
}
