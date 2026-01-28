import math
import random
import time
from enum import Enum


class Agent:
    ident = 0

    def __init__(self):
        self.id = Agent.ident
        Agent.ident += 1

    def get_chosen_action(self, state, max_depth):
        pass


class RandomAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        return actions[random.randint(0, len(actions) - 1)]


class GreedyAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        best_score, best_action = None, None
        for action in actions:
            new_state = state.generate_successor_state(action)
            score = new_state.get_score(state.get_on_move_chr())
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action


class MaxNAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        # best score vector and action which leads to it
        def maxn(state, depth):
            # if terminal or max depth or max rounds, return score vector and action which leads to it
            if state.is_goal_state() or state.get_current_round() == state.get_max_rounds() or depth==0:
                scores = state.get_scores()
                return [scores.get(chr(ord('A') + i), 0) for i in range(state.get_num_of_players())], None

            player = state.get_on_move_ord()  # who is on move
            best_scores=[-math.inf for i in range(state.get_num_of_players())]
            best_action = None
            actions = state.get_legal_actions()
            for action in actions:
                new_state = state.generate_successor_state(action)
                scores, _ = maxn(new_state, depth-1)
                if scores[player]>best_scores[player]:
                    best_scores = scores
                    best_action = action
            return best_scores, best_action

        time.sleep(0.5)
        _, action=maxn(state, max_depth)
        return action


class MinimaxAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        #best score and action which leads to it
        def minimax(state, depth, player_agent, player_on_move):
            #if terminal
            if state.is_goal_state() or state.get_current_round() == state.get_max_rounds()or depth==0:
                opponent = 1 - player_agent  # cause we have two players
                #the evaluation function is the difference between the agent's result and the opponents
                scores=state.get_scores()
                playerScore=scores.get(chr(ord('A') + player_agent), 0)
                opponentScore=scores.get(chr(ord('A') + opponent), 0)
                return playerScore-opponentScore, None

            if player_agent==player_on_move: #max player
                best_score=-math.inf
                best_action = None
                actions = state.get_legal_actions()
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    score, _ = minimax(new_state, depth-1, player_agent, new_state.get_on_move_ord())
                    if score>best_score:
                        best_score=score
                        best_action = action
                return best_score, best_action
            else: #min player
                best_score=math.inf
                best_action = None
                actions = state.get_legal_actions()
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    score, _ = minimax(new_state, depth-1, player_agent, new_state.get_on_move_ord())
                    if score<best_score:
                        best_score=score
                        best_action = action
                return best_score, best_action

        time.sleep(0.5)
        agent=state.get_on_move_ord()
        _, action=minimax(state, max_depth, agent, agent)
        return action

class MinimaxABAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        # best score and action which leads to it
        def minimax_alpha_beta(state, depth, player_agent, player_on_move, alpha, beta):
            # if terminal
            if state.is_goal_state() or state.get_current_round() == state.get_max_rounds() or depth == 0:
                opponent = 1 - player_agent  # cause we have two players
                # the evaluation function is the difference between the agent's result and the opponents
                scores = state.get_scores()
                playerScore = scores.get(chr(ord('A') + player_agent), 0)
                opponentScore = scores.get(chr(ord('A') + opponent), 0)
                return playerScore - opponentScore, None

            if player_agent == player_on_move:  # max player
                best_score = -math.inf
                best_action = None
                actions = state.get_legal_actions()
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    score, _ = minimax_alpha_beta(new_state, depth - 1, player_agent, new_state.get_on_move_ord(), alpha, beta)
                    if score > best_score:
                        best_score = score
                        best_action = action
                    alpha=max(alpha, score)
                    if alpha>=beta: #alpha cut
                        break
                return best_score, best_action
            else:  # min player
                best_score = math.inf
                best_action = None
                actions = state.get_legal_actions()
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    score, _ = minimax_alpha_beta(new_state, depth - 1, player_agent, new_state.get_on_move_ord(), alpha, beta)
                    if score < best_score:
                        best_score = score
                        best_action = action
                    beta=min(beta, score)
                    if alpha>=beta: #beta cut
                        break
                return best_score, best_action

        time.sleep(0.5)
        agent=state.get_on_move_ord()
        _, action=minimax_alpha_beta(state, max_depth, agent, agent, -math.inf, math.inf)
        return action


