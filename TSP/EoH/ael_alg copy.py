import numpy as np

def get_matrix_and_nodes(distance_matrix, local_opt_tour, global_opt_tour, edge_n_used):
    new_distance_matrix = np.copy(distance_matrix)

    impact = np.zeros(distance_matrix.shape[0])
    for i in range(len(local_opt_tour) - 1):
        # Updating distance matrix based on local optimal tour
        new_distance_matrix[local_opt_tour[i], local_opt_tour[i+1]] += edge_n_used[local_opt_tour[i], local_opt_tour[i+1]]
        new_distance_matrix[local_opt_tour[i+1], local_opt_tour[i]] += edge_n_used[local_opt_tour[i+1], local_opt_tour[i]]
        
        # Updating distance matrix based on global optimal tour
        new_distance_matrix[global_opt_tour[i], global_opt_tour[i+1]] += edge_n_used[global_opt_tour[i], global_opt_tour[i+1]]
        new_distance_matrix[global_opt_tour[i+1], global_opt_tour[i]] += edge_n_used[global_opt_tour[i+1], global_opt_tour[i]]

        # Calculating impact of perturbing each node
        impact[local_opt_tour[i]] += np.sum(new_distance_matrix[local_opt_tour[i], :]) + np.sum(new_distance_matrix[:, local_opt_tour[i]]) - new_distance_matrix[local_opt_tour[i], local_opt_tour[i]]
        impact[local_opt_tour[i+1]] += np.sum(new_distance_matrix[local_opt_tour[i+1], :]) + np.sum(new_distance_matrix[:, local_opt_tour[i+1]]) - new_distance_matrix[local_opt_tour[i+1], local_opt_tour[i+1]]

        impact[global_opt_tour[i]] += np.sum(new_distance_matrix[global_opt_tour[i], :]) + np.sum(new_distance_matrix[:, global_opt_tour[i]]) - new_distance_matrix[global_opt_tour[i], global_opt_tour[i]]
        impact[global_opt_tour[i+1]] += np.sum(new_distance_matrix[global_opt_tour[i+1], :]) + np.sum(new_distance_matrix[:, global_opt_tour[i+1]]) - new_distance_matrix[global_opt_tour[i+1], global_opt_tour[i+1]]

    perturb_nodes = np.argsort(impact)
        
    return new_distance_matrix, perturb_nodes