def fuse_domain_experts(
    expert_scores: dict[str, dict[str, float]],
    domain_weights: dict[str, float],
    fusion_method: str
) -> float:
    """
    Fuse multiple domain expert models into a single score.
    
    Args:
        expert_scores: Dict of expert_name -> {domain: score}
        domain_weights: Dict of domain -> importance weight
        fusion_method: 'weighted_average' or 'best_per_domain'
    
    Returns:
        Overall fused score (weighted by domain importance)
    """
    
    fused_domain_scores = {}
    
    for domain in domain_weights:
        # Collect all expert scores for this domain
        scores = [expert_scores[expert][domain] for expert in expert_scores]
        
        if fusion_method == "best_per_domain":
            fused_domain_scores[domain] = max(scores)
        
        elif fusion_method == "weighted_average":
            total = sum(scores)
            
            if total == 0:
                fused_domain_scores[domain] = 0.0
       